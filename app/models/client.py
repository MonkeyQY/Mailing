from pydantic import BaseModel


class Client(BaseModel):
    id: int
    mobile_number: int
    mobile_operator_code: str
    tag: str
    utc: int


class ClientAdd(BaseModel):
    mobile_number: int
    mobile_operator_code: str
    tag: str
    utc: int


class ClientUpdate(BaseModel):
    id: int
    mobile_number: int
    mobile_operator_code: str
    tag: str
    utc: int


class ClientDelete(BaseModel):
    id: int


class ClientAddResponse(BaseModel):
    id: int
    mobile_number: int
    mobile_operator_code: str
    tag: str
    utc: str
    message: str


class ClientUpdateResponse(BaseModel):
    mobile_number: int
    mobile_operator_code: str
    tag: str
    utc: str
    message: str

    class Config:
        schema_extra = {
            "example": {
                "mobile_number": 79123456789,
                "mobile_operator_code": "380",
                "tag": "tag",
                "utc": '+1',
                "message": "Client updated"
            }
        }


class ClientDeleteResponse(BaseModel):
    id: int
    message: str
