from datetime import datetime

from pydantic import BaseModel


class Message(BaseModel):
    id: int
    mailing_id: int
    client_id: int
    created_at: datetime
    sending_status: bool
