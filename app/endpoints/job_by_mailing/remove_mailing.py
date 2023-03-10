import logging

from fastapi import APIRouter, HTTPException, Depends

from app import config
from app.depends.depend_mailing import get_mailing_repository
from app.models.mailing import MailingDelete, MailingDeleteResponse
from app.repositories.mailing_repository import MailingRepository

router = APIRouter()

log = logging.getLogger("MailingRemove")


@router.delete(config.remove_mailing_path, response_model=MailingDeleteResponse)
async def remove_mailing(
    mailing: MailingDelete,
    mailing_repository: MailingRepository = Depends(get_mailing_repository),
) -> MailingDeleteResponse:
    log.info(f"Remove mailing request received, mailing: {mailing.id}")

    try:
        await mailing_repository.delete(mailing)
        log.info(f"Mailing {mailing.id} successfully removed")

    except Exception:
        log.info("Mailing not found")
        raise HTTPException(status_code=404, detail="Mailing not found")

    return MailingDeleteResponse(id=mailing.id, message="Mailing removed")
