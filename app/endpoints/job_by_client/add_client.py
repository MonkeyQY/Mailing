import logging

from fastapi import APIRouter, Request, Response, HTTPException, Depends

from app import config
from app.depends.depend_client import get_client_repository
from app.models.client import ClientAddResponse, ClientAdd
from app.repositories.client_repository import ClientRepository

router = APIRouter()

log = logging.getLogger("ClientAdd")


@router.post(config.add_client_path, response_model=ClientAddResponse)
async def add_client(
        client: ClientAdd,
        client_repository: ClientRepository = Depends(get_client_repository)):
    log.info(f"Received client: {client}")

    try:
        client_id = await client_repository.create(client)
        log.info(f"Client {client_id} was added")

        client_new = await client_repository.get_by_id(client_id)

    except HTTPException as e:
        log.info(f"Error: {e} for client: {client}")
        raise HTTPException(status_code=e.status_code, detail=e.detail)

    return ClientAddResponse(message=f"Client added, id: {client_new.id}",
                             id=client_new.id,
                             mobile_number=client_new.mobile_number,
                             mobile_operator_code=client_new.mobile_operator_code,
                             tag=client_new.tag,
                             utc=client_new.utc)
