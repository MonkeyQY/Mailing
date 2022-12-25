import asyncio
import datetime
import logging

import aiohttp
from fastapi import Depends

from app import config
from app.depends.depend_client import get_client_repository
from app.depends.depend_mailing import get_mailing_repository
from app.depends.depend_message import get_message_repository
from app.models.client import Client
from app.models.mailing import Mailing
from app.models.message import Message
from app.repositories.client_repository import ClientRepository
from app.repositories.mailing_repository import MailingRepository
from app.repositories.message_repository import MessageRepository
from app.scheduler.scheduler import schedule

log = logging.getLogger("SendMail")


class SendMail:

    def __init__(self,
                 mailing: Mailing,
                 mailing_repository: MailingRepository = Depends(get_mailing_repository)):
        self.mailing = mailing
        self.mailing_repository = mailing_repository

    @classmethod
    async def start_scheduler(cls, mailing: Mailing):
        await cls(mailing)._start_sends()

    async def _get_clients(
            self,
            clients_repository: ClientRepository = Depends(get_client_repository)):
        clients = await clients_repository.get_clients_where_pattern(self.mailing.filter)
        clients = [client for client in clients if
                   (datetime.datetime.utcnow() + datetime.timedelta(int(client.utc))).hour
                   == self.mailing.time_sending]
        return clients

    async def _start_sends(self):
        clients = await self._get_clients()

        async with asyncio.TaskGroup as task_group:
            async with aiohttp.ClientSession as session:
                for client in clients:
                    task_group.create_task(self._send_to_client(client, session))

        await self.mailing_repository.end_time_mailing(self.mailing.id)

    async def _send_to_client(self, client: Client, session: aiohttp):
        headers = {
            'accept': 'application/json',
            'Authorization': "Bearer " + config.jwt_token,
            'Content-Type': 'application/json',
        }

        message_id = await self._create_message(client.id)

        json_data = {
            'id': message_id,
            'phone': client.mobile_number,
            'text': self.mailing.text_message,
        }
        log.info(f"Create message {message_id} for client {client.id}, mailing {self.mailing.id}")

        url = config.url_for_send + "/" + message_id
        response = await session.post(url, headers=headers, json=json_data)

        if response.status != 200:
            log.info(f"Error: {response} for client: {client}")
            # TODO add error handling
            return
        await self._update_message(message_id)
        log.info(f'Send message to client {client.id} with response {response},'
                 f'mailing {self.mailing.id} - message {message_id}')

    async def _create_message(
            self,
            client_id: int,
            message_repository: MessageRepository = Depends(get_message_repository)):
        return await message_repository.create(client_id, self.mailing.id)

    @staticmethod
    async def _update_message(
            message_id: int,
            message_repository: MessageRepository = Depends(get_message_repository)):
        return await message_repository.change_status(message_id)

    @staticmethod
    async def stop_scheduler(mailing_id: int):
        schedule.remove_job(mailing_id)
