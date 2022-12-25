import datetime

from pydantic import BaseModel


class Mailing(BaseModel):
    id: int
    filter: str
    text_message: str
    time_sending: int
    updated_at: datetime.datetime
    start_time: dict
    end_time: dict


class MailingAdd(BaseModel):
    filter: str
    text_message: str
    time_sending: int
    start_time: dict
    end_time: dict

    class Config:

        schema_extra = {
            "example": {
                "filter": "tag or mobile operator code",
                "text_message": "Hello",
                "start_time": {
                    "year": 2021,
                    "month": 5,
                    "day": 1,
                    "hour": 0,
                    "minute": 0,
                    "second": 0
                },
                "end_time": {
                    "year": 2021,
                    "month": 5,
                    "day": 1,
                    "hour": 0,
                    "minute": 0,
                    "second": 0
                },
            }
        }


class MailingUpdate(BaseModel):
    id: int
    time_sending: int
    filter: str
    text_message: str
    start_time: dict
    end_time: dict

    class Config:

        schema_extra = {
            "example": {
                "id": 1,
                "filter": "tag or mobile operator code",
                "text_message": "Hello",
                "start_time": {
                    "year": 2021,
                    "month": 5,
                    "day": 1,
                    "hour": 0,
                    "minute": 0,
                    "second": 0
                },
                "end_time": {
                    "year": 2021,
                    "month": 5,
                    "day": 1,
                    "hour": 0,
                    "minute": 0,
                    "second": 0
                },
            }
        }


class MailingDelete(BaseModel):
    id: int


class MailingAddResponse(BaseModel):
    id: int
    filter: str
    text_message: str
    start_time: dict
    end_time: dict
    time_sending: int
    message: str

    class Config:

        schema_extra = {
            "example": {
                "id": 1,
                "filter": "age > 18",
                "text_message": "Hello",
                "start_time": {
                    "year": 2021,
                    "month": 5,
                    "day": 1,
                    "hour": 0,
                    "minute": 0,
                    "second": 0
                },
                "end_time": {
                    "year": 2021,
                    "month": 5,
                    "day": 1,
                    "hour": 0,
                    "minute": 0,
                    "second": 0
                },
                "message": "Mailing updated successfully",
            }
        }


class MailingUpdateResponse(BaseModel):
    filter: str
    text_message: str
    time_sending: int
    start_time: str
    end_time: str
    message: str


class MailingDeleteResponse(BaseModel):
    id: int
    message: str
