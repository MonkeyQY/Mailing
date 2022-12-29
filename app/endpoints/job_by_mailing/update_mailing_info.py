import logging

from fastapi import APIRouter, HTTPException, Depends

from app import config
from app.datetime_trasformation.get_tuple_datetime import MyDatetime
from app.depends.depend_mailing import get_mailing_repository
from app.endpoints.job_by_mailing.add_new_mailing import StartMailing
from app.models.mailing import MailingUpdateResponse, MailingUpdate
from app.repositories.mailing_repository import MailingRepository

router = APIRouter()

log = logging.getLogger("MailingUpdate")


@router.put(config.update_mailing_path, response_model=MailingUpdateResponse)
async def update_mailing_info(
    mailing: MailingUpdate,
    mailing_repository: MailingRepository = Depends(get_mailing_repository),
) -> MailingUpdateResponse:
    log.info(f"Update mailing request received, mailing: {mailing.id}")

    try:
        await mailing_repository.update(mailing)
        log.info(f"Mailing {mailing.id} successfully updated")

        mailing_new = await mailing_repository.get_by_id(mailing.id)
    except Exception:
        log.info("Mailing not found")
        raise HTTPException(status_code=404, detail="Mailing not found")
    try:
        await StartMailing.start_mail(mailing_new)
    except Exception as e:
        log.info(f"Mailing not started, {e}")

    start_time = MyDatetime.get_str_for_dict_date(mailing_new.start_time)
    end_time = MyDatetime.get_str_for_dict_date(mailing_new.end_time)

    return MailingUpdateResponse(
        id=mailing.id,
        message="Mailing updated",
        text_message=mailing_new.text_message,
        filter=mailing_new.filter,
        time_sending=mailing_new.time_sending,
        start_time=start_time,
        end_time=end_time,
    )
