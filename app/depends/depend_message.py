from app.db import database
from app.repositories.message_repository import MessageRepository


def get_message_repository() -> MessageRepository:
    return MessageRepository(database)
