import logging

from fastapi import APIRouter, Request, Response, HTTPException, Depends

from app import config
from app.depends.depend_mailing import get_mailing_repository
from app.models.mailing import MailingUpdateResponse, MailingUpdate
from app.repositories.mailing_repository import MailingRepository

router = APIRouter()

log = logging.getLogger("MailingUpdate")


@router.put(config.add_client_path, response_model=MailingUpdateResponse)
def update_mailing_info(mailing: MailingUpdate,
                        mailing_repository: MailingRepository = Depends(get_mailing_repository)):
    log.info(f'Update mailing request received, mailing: {mailing.id}')

    try:
        mailing_id = await mailing_repository.update(mailing)
        log.info(f'Mailing {mailing.id} successfully updated')

        mailing_new = await mailing_repository.get_by_id(mailing_id)
    except Exception as e:
        log.info('Mailing not found')
        raise HTTPException(status_code=404, detail="Mailing not found")

    return MailingUpdateResponse(id=mailing.id, message='Mailing updated', text_message=mailing_new.text_message,
                                 filter=mailing_new.filter)
