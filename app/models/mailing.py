from pydantic import BaseModel


class Mailing(BaseModel):
    id: int
    filter: str
    text_message: str
    start_time: str
    end_time: str


class MailingAdd(BaseModel):
    filter: str
    text_message: str
    start_time: str
    end_time: str


class MailingUpdate(BaseModel):
    id: int
    filter: str
    text_message: str
    start_time: str
    end_time: str


class MailingDelete(BaseModel):
    id: int


class MailingAddResponse(BaseModel):
    id: int
    filter: str
    text_message: str
    start_time: str
    end_time: str
    message: str


class MailingUpdateResponse(BaseModel):
    filter: str
    text_message: str
    start_time: str
    end_time: str
    message: str


class MailingDeleteResponse(BaseModel):
    id: int
    message: str
