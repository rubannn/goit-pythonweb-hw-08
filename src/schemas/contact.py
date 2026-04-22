from pydantic import BaseModel


class ContactBase(BaseModel):
    first_name: str
