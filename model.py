from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class DBManager(BaseModel):
    username: str
    password: str