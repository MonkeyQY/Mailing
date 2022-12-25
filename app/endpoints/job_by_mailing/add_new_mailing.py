import logging
from datetime import datetime

from fastapi import APIRouter, HTTPException, Depends

from app import config
from app.datetime_trasformation.get_tuple_datetime import MyDatetime
from app.depends.depend_mailing import get_mailing_repository
from app.models.mailing import MailingAddResponse, MailingAdd, Mailing
from app.repositories.mailing_repository import MailingRepository
from app.scheduler.scheduler import schedule
from app.start_mailing.start_mailing import SendMail

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

    except Exception as e:
        log.info(f'Mailing not added, {e}')
        raise HTTPException(status_code=400, detail="Mailing not added")

    try:
        await StartMailing.start_mail(mailing_new)
    except Exception as e:
        log.info(f'Mailing not started, {e}')

    start_time = MyDatetime.get_str_for_tuple_date(mailing_new.start_time)
    end_time = MyDatetime.get_str_for_tuple_date(mailing_new.end_time)

    return MailingAddResponse(id=mailing_new.id,
                              text_message=mailing_new.text_message,
                              filter=mailing_new.filter,
                              start_time=start_time,
                              end_time=end_time,
                              message="Mailing successfully added",
                              time_sending=mailing_new.time_sending)


class StartMailing:

    def __init__(self, mailing: Mailing):
        self.mailing = mailing
        self.start_time: tuple = MyDatetime.get_tuple_datetime(self.mailing.start_time)
        self.end_time: tuple = MyDatetime.get_tuple_datetime(self.mailing.end_time)

    @classmethod
    async def start_mail(cls, mailing: Mailing):
        await cls(mailing)._start()

    async def _start(self):
        start_time = datetime(
            self.start_time[0],
            self.start_time[1],
            self.start_time[2],
            self.start_time[3],
            self.start_time[4],
            self.start_time[5])
        end_time = datetime(
            self.end_time[0],
            self.end_time[1],
            self.end_time[2],
            self.end_time[3],
            self.end_time[4],
            self.end_time[5])
        # if start_time < datetime.utcnow() < end_time:
        if start_time < datetime.now() < end_time:
            await SendMail.start_scheduler(self.mailing)
            await self._stop_scheduler(end_time)
        else:
            await self._start_scheduler(start_time, end_time)

    async def _start_scheduler(self, start_time: datetime, end_time: datetime):
        # TODO add scheduler
        print(start_time)
        schedule.add_job(
            SendMail.start_scheduler,
            'date',
            args=(self.mailing,),
            run_date=start_time,
            id=str(self.mailing.id) + 'start',
            replace_existing=True)

        await self._stop_scheduler(end_time)

    async def _stop_scheduler(self, end_time: datetime):
        schedule.add_job(
            SendMail.stop_scheduler,
            'date',
            args=(self.mailing.id,),
            run_date=end_time,
            id=str(self.mailing.id) + 'stop',
            replace_existing=True)
