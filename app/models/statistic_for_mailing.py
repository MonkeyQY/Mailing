from pydantic import BaseModel


class StatisticMailingResponse(BaseModel):
    mailings: dict

    class Config:
        schema_extra = {
            "example": {
                "mailings": {
                    "mailing1": [
                        {
                            "message_id": 1,
                            "mailing_id": 1,
                            "sending_status": True,
                            "client_id": 1,
                            "created_at": "2021-05-01 00:00:00",
                        },
                        {
                            "message_id": 2,
                            "mailing_id": 1,
                            "sending_status": False,
                            "client_id": 2,
                            "created_at": "2021-05-01 00:00:00",
                        },
                    ],
                    "mailing2": [
                        {
                            "message_id": 3,
                            "mailing_id": 2,
                            "sending_status": True,
                            "client_id": 1,
                            "created_at": "2021-05-01 00:00:00",
                        },
                        {
                            "message_id": 4,
                            "mailing_id": 2,
                            "sending_status": False,
                            "client_id": 2,
                            "created_at": "2021-05-01 00:00:00",
                        },
                    ],
                    "mailing3": [
                        {
                            "message_id": 4,
                            "mailing_id": 3,
                            "sending_status": True,
                            "client_id": 1,
                            "created_at": "2021-05-01 00:00:00",
                        },
                        {
                            "message_id": 5,
                            "mailing_id": 3,
                            "sending_status": False,
                            "client_id": 2,
                            "created_at": "2021-05-01 00:00:00",
                        },
                    ],
                }
            }
        }


class DetailStatistic(BaseModel):
    mailing_id: int


class DetailStatisticResponse(BaseModel):
    statistics: dict

    class Config:
        schema_extra = {
            "example": {
                "statistics": {
                    "mailing_id": 1,
                    "filter": "tag or mobile operator code",
                    "messages": [
                        {
                            "message_id": 1,
                            "mailing_id": 1,
                            "sending_status": True,
                            "client_id": 1,
                            "created_at": "2021-05-01 00:00:00",
                        },
                        {
                            "message_id": 2,
                            "mailing_id": 1,
                            "sending_status": False,
                            "client_id": 2,
                            "created_at": "2021-05-01 00:00:00",
                        },
                    ],
                    "time_sending": 1,
                    "start_time": "2021-05-01 00:00:00",
                    "end_time": "2021-05-01 00:00:00",
                    "updated_at": "2021-05-01 00:00:00",
                }
            }
        }
