from app.db import database
from app.repositories.mailing_repository import MailingRepository


def get_mailing_repository() -> MailingRepository:
    return MailingRepository(database)