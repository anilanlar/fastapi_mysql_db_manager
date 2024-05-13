from pydantic import BaseModel
from typing import List

class Player(BaseModel):
    username: str
    position_id: int

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
    
class CreateSquad(BaseModel):
    session_id: int
    coach_username: str
    players:  List[Player]
    
class RateSession(BaseModel):
    session_id: int
    jury_username: str
    rating: int
    
class PlayedPlayer(BaseModel):
    username: str

class PlayerInfo(BaseModel):
    name: str
    surname: str

class FrequentPlayer(BaseModel):
    name: str
    surname: str
    count: int

class PlayerStats(BaseModel):
    played_with: List[PlayerInfo]
    most_frequent: List[FrequentPlayer]
    average_height: float
    
