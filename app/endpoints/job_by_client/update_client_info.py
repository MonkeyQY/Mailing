import logging

from fastapi import APIRouter, Request, Response, HTTPException, Depends

from app import config
from app.depends.depend_client import get_client_repository
from app.models.client import ClientUpdate, ClientUpdateResponse
from app.repositories.client_repository import ClientRepository

router = APIRouter()

log = logging.getLogger("ClientUpdate")


@router.put(config.update_client_path, response_model=ClientUpdateResponse)
async def update_client(
        client: ClientUpdate,
        client_repository: ClientRepository = Depends(get_client_repository)):
    log.info(f'Update client request received, client: {client.id}')

    try:
        await client_repository.update(client)
        log.info(f'Client {client.id} successfully updated')

        client_new = await client_repository.get_by_id(client.id)
    except Exception as e:
        log.info(f'Client not found, {e}')
        raise HTTPException(status_code=404, detail="Client not found")

    return ClientUpdateResponse(
        id=client_new.id,
        message='Client updated',
        mobile_number=client_new.mobile_number,
        mobile_operator_code=client_new.mobile_operator_code,
        tag=client_new.tag,
        utc=client_new.utc)
