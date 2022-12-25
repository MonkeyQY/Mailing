import logging
from datetime import datetime

from fastapi import APIRouter, HTTPException, Depends

from app import config
from app.datetime_trasformation.get_tuple_datetime import MyDatetime
from app.depends.depend_mailing import get_mailing_repository
from app.depends.depend_message import get_message_repository
from app.models.mailing import Mailing
from app.models.statistic_for_mailing import DetailStatistic, DetailStatisticResponse
from app.repositories.mailing_repository import MailingRepository
from app.repositories.message_repository import MessageRepository

router = APIRouter()

log = logging.getLogger("DetailForTheMailing")


@router.post(config.detail_mailing_path, response_model=DetailStatisticResponse)
async def detail_for_the_mailing(mailing: DetailStatistic):
    log.info(f'Detail for the mailing request received, mailing: {mailing.mailing_id}')

    try:
        statistics = \
            await GetStatisticsForMailing.get_statistics_for_mailing(mailing.mailing_id)
        log.info(f'Mailing {mailing.mailing_id} successfully added')
    except Exception as e:
        log.info(f'Mailing not added, {e}')
        raise HTTPException(status_code=400, detail="Mailing not added")

    return DetailStatisticResponse(statistics=statistics)


class GetStatisticsForMailing:
    def __init__(self,
                 mailing_repository: MailingRepository = get_mailing_repository(),
                 message_repository: MessageRepository = get_message_repository()):
        self.mailing_repository = mailing_repository
        self.message_repository = message_repository

    @classmethod
    async def get_statistics_for_mailing(cls, mailing_id: int):
        return await cls().get_detail_for_the_mailing(mailing_id)

    async def get_detail_for_the_mailing(self, mailing_id: int) -> dict:
        mailing: Mailing = await self.mailing_repository.get_by_id(mailing_id)

        messages = await self.message_repository.get_all_messages_for_mailing(mailing_id)

        list_messages = []
        for message in messages:
            dict_message = {
                'message_id': message.sending_status,
                'client_id': message.client_id,
                'created_at': message.created_at,
                'sending_status': message.sending_status
            }

            list_messages.append(dict_message)

        statistics = {
            'mailing_id': mailing_id,
            'filter': mailing.filter,
            'messages': list_messages,
            'time_sending': mailing.time_sending,
            'start_time': MyDatetime.get_datetime(mailing.start_time),
            'end_time': MyDatetime.get_datetime(mailing.end_time),
            'updated_at': mailing.updated_at
        }

        return statistics

