from fastapi import APIRouter, Request, Response, HTTPException

from app import config

router = APIRouter()

@router.get(config.add_client_path)
def detail_for_the_mailing():
    pass