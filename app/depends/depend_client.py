from app.db import database
from app.repositories.client_repository import ClientRepository


def get_client_repository() -> ClientRepository:
    return ClientRepository(database)