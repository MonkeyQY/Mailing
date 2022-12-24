from fastapi import APIRouter, Request, Response, HTTPException

from app import config

router = APIRouter()


@router.get(config.add_client_path)
def total_for_mailings():
    pass
