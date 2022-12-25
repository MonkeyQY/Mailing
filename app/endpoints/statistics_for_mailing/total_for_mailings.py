from dataclasses import dataclass
import logging
from typing import Optional

from fastapi import APIRouter, Request, Response, HTTPException, Depends

from app import config
from app.depends.depend_mailing import get_mailing_repository
from app.depends.depend_message import get_message_repository
from app.models.mailing import Mailing
from app.models.message import Message
from app.models.statistic_for_mailing import StatisticMailingResponse
from app.repositories.mailing_repository import MailingRepository
from app.repositories.message_repository import MessageRepository

router = APIRouter()

log = logging.getLogger("TotalMailings")


@router.get(config.total_mailing_path, response_model=StatisticMailingResponse)
async def total_for_mailings():
    log.info('Total for mailings request received')

    try:
        statistics = await GetStatistic.get_statistic()
        log.info('Total for mailings request successful')

    except ValueError:
        log.info('Total for mailings request failed')
        raise HTTPException(status_code=400, detail="Wrong data")

    return StatisticMailingResponse(mailings=statistics)


class GetStatistic:

    def __init__(self,
                 mailing_repository: MailingRepository = get_mailing_repository(),
                 message_repository: MessageRepository = get_message_repository()):
        self.mailing_repository = mailing_repository
        self.message_repository = message_repository
        self.all_mailings: Optional[list[Mailing]] = None

    @classmethod
    async def get_statistic(cls):
        return await cls()._get_statistic_for_all_mailings()

    async def _get_statistic_for_all_mailings(self) -> dict:
        await self._get_total_for_mailings()

        statistic = {}
        for mailing in self.all_mailings:
            list_message = await self._get_messages_for_the_mailing(mailing.id)
            statistic[mailing.id] = await self._group_by_sending_status(list_message)

        return statistic

    async def _get_total_for_mailings(self):
        self.all_mailings = await self.mailing_repository.get_all()

    async def _get_messages_for_the_mailing(self, mailing_id: int):
        list_messages = \
            await self.message_repository.get_all_messages_for_mailing(mailing_id)
        return list_messages

    async def _group_by_sending_status(self, list_messages: list[Message]) -> dict:
        list_sending_status_true = []
        list_sending_status_false = []

        for message in list_messages:
            if message.sending_status:
                list_sending_status_true.append(self._message_to_dict(message))
            else:
                list_sending_status_false.append(self._message_to_dict(message))

        return await self._from_list_messages_to_dict(
            list_sending_status_false,
            list_sending_status_true)

    @staticmethod
    async def _from_list_messages_to_dict(
            list_sending_status_false,
            list_sending_status_true) -> dict:
        dict_of_messages = {
            'sending_status_false': list_sending_status_false,
            'sending_status_true': list_sending_status_true
        }
        return dict_of_messages

    @staticmethod
    def _message_to_dict(message: Message) -> dict:
        dict_message = {
            "mailing_id": message.mailing_id,
            'message_id': message.id,
            'sending_status': message.sending_status,
            'client_id': message.client_id,
            'created_at': message.created_at,
        }

        return dict_message
