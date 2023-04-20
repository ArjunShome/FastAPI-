from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    address: str
    adhar_number: int
    mobile_number: int
    pan_number: int
    is_adult: bool
    