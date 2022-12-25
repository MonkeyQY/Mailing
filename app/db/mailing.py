import sqlalchemy
from sqlalchemy import Integer, Column, Text, String, JSON, DateTime

from app.db import db

mailings = sqlalchemy.Table(
    'mailing',
    db.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('filter', String),
    Column('text_message', Text),
    Column('time_sending', Integer),
    Column('update_at', DateTime),
    Column('end_time', JSON),
    Column('start_time', JSON),
)
