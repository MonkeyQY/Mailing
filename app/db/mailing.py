import sqlalchemy
from sqlalchemy import Integer, Column, Text, String, JSON, DateTime, func

from app.db import db

mailings = sqlalchemy.Table(
    "mailing",
    db.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("filter", String),
    Column("text_message", Text),
    Column("time_sending", Integer),
    Column(
        "updated_at",
        DateTime(timezone=False),
        onupdate=func.now(),
        server_default=func.now(),
    ),
    Column("end_time", JSON),
    Column("start_time", JSON),
)
