import logging
from datetime import datetime, timedelta

from fastapi import APIRouter, Request, Response, HTTPException, Depends

from app import config
from app.datetime_trasformation.get_tuple_datetime import MyDatetime
from app.depends.depend_client import get_client_repository
from app.depends.depend_mailing import get_mailing_repository
from app.models.mailing import MailingAddResponse, MailingAdd, Mailing
from app.repositories.client_repository import ClientRepository
from app.repositories.mailing_repository import MailingRepository
from app.scheduler.scheduler import schedule
from start_mailing.start_mailing import SendMail

router = APIRouter()

log = logging.getLogger("MailingAdd")


@router.post(config.add_new_mailing_path, response_model=MailingAddResponse)
async def add_new_mailing(
        mailing: MailingAdd,
        mailing_repository: MailingRepository = Depends(get_mailing_repository)):
    log.info(f'Add mailing request received, mailing: {mailing.text_message}')

    try:
        mailing_id = await mailing_repository.create(mailing)
        log.info(f'Mailing {mailing_id} successfully added')

        mailing_new = await mailing_repository.get_by_id(mailing_id)

        await StartMailing.start_mail(mailing_new)
    except Exception as e:
        log.info(f'Mailing not added, {e}')
        raise HTTPException(status_code=400, detail="Mailing not added")

    return MailingAddResponse(id=mailing_new.id,
                              text_message=mailing_new.text_message,
                              filter=mailing_new.filter,
                              start_time=MyDatetime.get_tuple_datetime(mailing_new.start_time),
                              end_time=MyDatetime.get_tuple_datetime(mailing_new.end_time),
                              message="Mailing successfully added",
                              time_sending=mailing_new.time_sending)


class StartMailing:

    def __init__(self, mailing: Mailing):
        self.mailing = mailing
        self.dates: tuple = MyDatetime.get_tuple_datetime(self.mailing.start_time)

    @classmethod
    async def start_mail(cls, mailing: Mailing):
        await cls(mailing)._start()

    async def _start(self):
        start_time = datetime(
            self.dates[0],
            self.dates[1],
            self.dates[2],
            self.dates[3],
            self.dates[4],
            self.dates[5])
        time_now = datetime.utcnow()
        if start_time > time_now:
            await self._start_scheduler(start_time)
        else:
            await SendMail.start_scheduler(self.mailing)

    async def _start_scheduler(self, start_time):
        # TODO add scheduler
        schedule.add_job(
            SendMail.start_scheduler,
            'date',
            [self.mailing],
            run_date=start_time,
            id=self.mailing.id)
