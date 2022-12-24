import logging

from fastapi import APIRouter, Request, Response, HTTPException, Depends

from app import config
from app.depends.depend_mailing import get_mailing_repository
from app.models.mailing import MailingAddResponse, MailingAdd
from app.repositories.mailing_repository import MailingRepository

router = APIRouter()

log = logging.getLogger("MailingAdd")


@router.post(config.add_client_path, response_model=MailingAddResponse)
def add_new_mailing(mailing: MailingAdd,
                    mailing_repository: MailingRepository = Depends(get_mailing_repository)):
    log.info(f'Add mailing request received, mailing: {mailing.text_message}')

    try:
        mailing_id = await mailing_repository.create(mailing)
        log.info(f'Mailing {mailing_id} successfully added')

        mailing_new = await mailing_repository.get_by_id(mailing_id)
    except Exception as e:
        log.info(f'Mailing not added, {e}')
        raise HTTPException(status_code=500, detail="Mailing not added")

    return MailingAddResponse(id=mailing_new.id,
                              message='Mailing added',
                              filter=mailing_new.filter,
                              text_message=mailing_new.text_message)
