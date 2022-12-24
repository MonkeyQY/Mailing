import sqlalchemy
from sqlalchemy import Integer, Column, Text, DateTime, String

from app.db import database

mailings = sqlalchemy.Table(
    'mailing',
    database.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('filter', String),
    Column('text_message', Text),
    Column('end_time', String),
    Column('start_time', String),
)
