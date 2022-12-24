import logging

# from app.db.users import users
# from app.db.notifications import notifications
# from app.db.patterns import patterns
# from app.db.balance import balance
from app.db.database import database, engine, metadata

log = logging.getLogger('main.database')

# если таблицы не существуют, то создаем их
if not engine.url:
    metadata.create_all(engine)
    log.info('Create tables in database')

log.info('Database created')