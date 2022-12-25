import logging

from app.db.client import clients
from app.db.mailing import mailings
from app.db.message import messages
from app.db.db import database, engine, metadata

log = logging.getLogger('main.database')

# если таблицы не существуют, то создаем их
metadata.create_all(engine)

log.info('Database created')