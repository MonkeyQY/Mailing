import logging

from fastapi import APIRouter, Request, Response, HTTPException, Depends

from app import config
from app.depends.depend_client import get_client_repository
from app.models.client import ClientDelete, ClientDeleteResponse
from app.repositories.client_repository import ClientRepository

router = APIRouter()

log = logging.getLogger("ClientRemove")


@router.delete(config.remove_client_path, response_model=ClientDeleteResponse)
async def remove_client(
        client: ClientDelete,
        client_repository: ClientRepository = Depends(get_client_repository)):
    log.info(f'Remove client request received, client: {client.id}')

    try:
        await client_repository.delete(client)
        log.info(f'Client {client.id} successfully removed')
    except Exception as e:
        log.info('Client not found')
        raise HTTPException(status_code=404, detail="Client not found")

    return ClientDeleteResponse(id=client.id, message='Client removed')
