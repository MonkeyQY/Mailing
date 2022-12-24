import logging

import uvicorn

from fastapi import FastAPI

from app.endpoints.job_by_client.add_client import router as job_by_add_client_router
from app.endpoints.job_by_client.remove_client import router as job_by_remove_client_router
from app.endpoints.job_by_client.update_client_info import router as job_by_update_client_router
from app.endpoints.job_by_mailing.add_new_mailing import router as job_by_add_mailing_router
from app.endpoints.job_by_mailing.remove_mailing import router as job_by_remove_mailing_router
from app.endpoints.job_by_mailing.update_mailing_info import router as job_by_update_mailing_router
from app.endpoints.statistics_for_mailing.total_for_mailings import router as statistics_for_total_mailing_router
from app.endpoints.statistics_for_mailing.detail_for_the_mailing import router as statistics_for_detail_mailing_router

from app import config
from app.db.database import database

# запись логов в файл


# logging.basicConfig(filename="logs.log", level=logging.INFO)
# log = logging.getLogger(__name__)

host = config.host
port = config.port

app = FastAPI(
    title="Listener",
    description="API for the application",
    version="1.0.0",
    docs_url=config.docs_url)

app.include_router(
    job_by_add_client_router, prefix=config.prefix_api, tags=["Job by client"])
app.include_router(
    job_by_update_client_router, prefix=config.prefix_api, tags=["Job by client"])
app.include_router(
    job_by_remove_client_router, prefix=config.prefix_api, tags=["Job by client"])

app.include_router(job_by_add_mailing_router, prefix=config.prefix_api, tags=["Job by mailing"])
app.include_router(
    job_by_update_mailing_router, prefix=config.prefix_api, tags=["Job by mailing"])
app.include_router(job_by_remove_mailing_router, prefix=config.prefix_api, tags=["Job by mailing"])

app.include_router(
    statistics_for_detail_mailing_router, prefix=config.prefix_api, tags=["Statistics for mailing"])
app.include_router(
    statistics_for_total_mailing_router, prefix=config.prefix_api, tags=["Statistics for mailing"])

logging.basicConfig(
    format='{asctime} : {levelname} : {name} : {message}', style='{', level=logging.INFO)

log = logging.getLogger("main")


@app.on_event("startup")
async def startup_event():
    await database.connect()
    log.info('Database connected')


@app.on_event("shutdown")
async def shutdown_event():
    await database.connect()
    log.info('Database disconnected')


if __name__ == '__main__':
    uvicorn.run("__main__:app",
                host=host,
                port=port,
                reload=True,
                log_config=None)
