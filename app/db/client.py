import sqlalchemy
from sqlalchemy import Integer, Column, String, BigInteger

from app.db import db

clients = sqlalchemy.Table(
    "clients",
    db.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("mobile_number", BigInteger),
    Column("mobile_operator_code", String),
    Column("tag", String),
    Column("utc", String),
)
