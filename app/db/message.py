from sqlalchemy import Integer, Column, ForeignKey, DateTime, Table, Boolean

from app.db import db

messages = Table(
    'messages',
    db.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('mailing_id', ForeignKey('mailing.id')),
    Column('client_id', ForeignKey('client.id')),
    Column('sending_status', Boolean),
    Column('create_at', DateTime),
)
