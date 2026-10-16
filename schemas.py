from pydantic import BaseModel, ConfigDict


class AuthorBase(BaseModel):
    name: str
    bio: str


class AuthorCreate(AuthorBase):
    pass

class AuthorRead(AuthorBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
