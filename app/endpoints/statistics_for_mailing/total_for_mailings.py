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
        statistics = GetStatistic.get_statistic()
        log.info('Total for mailings request successful')
    except ValueError:
        log.info('Total for mailings request failed')
        raise HTTPException(status_code=400, detail="Wrong data")

    return StatisticMailingResponse(mailings=statistics)


class GetStatistic:

    def __init__(self,
                 mailing_repository: MailingRepository = Depends(get_mailing_repository),
                 message_repository: MessageRepository = Depends(get_message_repository)):
        self.mailing_repository = mailing_repository
        self.message_repository = message_repository
        self.all_mailings: Optional[list[Mailing]] = None
        self.list_messages: Optional[list[Message]] = None
        self.list_sending_status_false = []
        self.list_sending_status_true = []

    @classmethod
    async def get_statistic(cls):
        return await cls()._get_statistic_for_all_mailings()

    async def _get_statistic_for_all_mailings(self) -> dict:
        await self._get_total_for_mailings()

        statistic = {}
        for mailing in self.all_mailings:
            await self._get_messages_for_the_mailing(mailing.id)
            statistic[mailing.id] = await self._group_by_sending_status()

        return statistic

    async def _get_total_for_mailings(self):
        self.all_mailings = await self.mailing_repository.get_all()

    async def _get_messages_for_the_mailing(self, mailing_id):
        self.list_messages = \
            await self.message_repository.get_all_messages_for_mailing(mailing_id)

    async def _group_by_sending_status(self):

        for message in self.list_messages:
            if message.sending_status:
                self.list_sending_status_true.append(self._message_to_dict(message))
            else:
                self.list_sending_status_false.append(self._message_to_dict(message))

        return await self._from_list_messages_to_dict()

    async def _from_list_messages_to_dict(self) -> dict:
        dict_of_messages = {
            'sending_status_false': self.list_sending_status_false,
            'sending_status_true': self.list_sending_status_true
        }
        return dict_of_messages

    @staticmethod
    async def _message_to_dict(message: Message) -> dict:
        dict_message = {message.id: {
            'mailing_id': message.mailing_id,
            'sending_status': message.sending_status,
            'client_id': message.client_id,
            'created_at': message.created_at,
        }}

        return dict_message
