from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class User(UserBase):
    id: int
    items: list = []
    
    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str
