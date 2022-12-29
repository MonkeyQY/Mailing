from sqlalchemy.engine import URL
from sqlalchemy import create_engine, MetaData
from databases import Database

from app.config import DATABASE

database_url = URL.create(**DATABASE)


database = Database(str(database_url))
metadata = MetaData()

engine = create_engine(database_url)
