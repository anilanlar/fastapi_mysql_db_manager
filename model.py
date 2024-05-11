from pydantic import BaseModel


class DBManager(BaseModel):
    username: str
    password: str
    
    
class DeleteSessionRequest(BaseModel):
    session_id: int
    
    
class AddMatchSession(BaseModel):
    coach_username: str
    stadium_id: int
    time_slot: int
    date: str
    jury_name: str
    jury_surname: str
    
class AddUserRequest(BaseModel):
    user_type: str
    username: str
    password: str
    name: str
    surname: str
    date_of_birth: str
    height: float
    weight: float
    nationality: str