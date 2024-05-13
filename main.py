from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from fastapi.middleware.cors import CORSMiddleware

import uvicorn
from database import create_tables,drop_tables,add_data
from query import *
from model import *

app = FastAPI()
app.add_middleware( # Adjusting CORS 
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,  
    allow_methods=["*"],     
    allow_headers=["*"],    
)
# Test api
# @app.post("/test-api",response_model = str)
# def hello_api():
#     return "Hello apppiiiii"

# Api for password check for login 
@app.post("/db-manager-login/", response_model= str)
def db_manager_login_api(db_manager: DBManager):
    try:
        print(db_manager.username, db_manager.password)
        if db_manager_login(db_manager.username, db_manager.password):
            return "DB LOGIN SUCCESS"
        else:
            raise HTTPException(status_code=401, detail="Invalid credentials")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Api for stadium name change
@app.post("/change-stadium-name/", response_model=str)
def change_stadium_name(dct: dict):
    try:
        if update_stadium_name(dct["old_name"], dct["new_name"]):
            return "Stadium name updated successfully"
        else:
            raise HTTPException(status_code=404, detail="Stadium not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Api for deleting match session
@app.post("/delete-match-session/", response_model=str)
def delete_match_session(session: DeleteSessionRequest):

    sId= session.session_id
    num_of_deleted_rows = delete_match_session_query(sId)
    if num_of_deleted_rows > 0:
        return "Match session deleted successfully >>> " + str(num_of_deleted_rows)+ " rows affected"
    else:
        return HTTPException(status_code=404, detail="Session not found")


# Api for creating squad 
@app.post("/create-squad/", response_model=str)
def create_squad(create_squad: CreateSquad):
    try:
        create_squad_query(create_squad.session_id, create_squad.coach_username, create_squad.players)
        return "Match session added successfully"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
    
# Api for adding new match session
@app.post("/add-match-session/", response_model=str)
def add_match_session(match_session: AddMatchSession):
    try:
        add_match_session_query(match_session.coach_username, match_session.stadium_id, match_session.time_slot, match_session.date, match_session.jury_name, match_session.jury_surname)
        return "Match session added successfully"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
# Api for fetching stadiums
@app.get("/get-stadiums")
def get_stadiums():
    try:
        stadiums = get_stadiums_query()  
        jsonResponse = {i: {'name': stadium[0], 'country': stadium[1]} for i, stadium in enumerate(stadiums)}
        # print(jsonResponse)
        return JSONResponse(content=jsonResponse)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Api for fetching stadiums
@app.post("/get-jury-ratings", response_model=dict)
def get_jury_ratings(jury: dict):
    try:
        ratings = get_jury_ratings_query(jury["jury_username"])
        jsonResponse= {}
        jsonResponse["average"] = ratings[0]
        jsonResponse["count"] = ratings[1] 
        return jsonResponse
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
# Api for adding new user
@app.post("/add-new-user/", response_model=str)
def add_new_user(user: AddUserRequest):
    try:
        add_new_user_query(user.user_type, user.username, user.password, user.name, user.surname, user.date_of_birth, user.height, user.weight, user.nationality)
        return "User added successfully"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

   
   
# Api for rating an existing session
@app.post("/rate-session/", response_model=str)
def rate_match(rated_session: RateSession):
    try:
        rate_match_query(rated_session.session_id, rated_session.jury_username, rated_session.rating)
        return "match rated successfully"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Api for getting player list that have played together
@app.post("/get-played-player/", response_model=PlayerStats)
def get_played_player(player: PlayedPlayer):
    try:
        players = view_played_players_query(player.username)# 
        played_with = [PlayerInfo(name=p[0], surname=p[1]) for p in players['played_with']] 
        most_frequent = [FrequentPlayer(name=p[0], surname=p[1], count=p[2]) for p in players['most_frequent']]
        average_height = players['average_height']
        return PlayerStats(played_with=played_with, most_frequent=most_frequent, average_height=average_height)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



if __name__ == "__main__":
    drop_tables()# Firstly drop all tables and clear db
    create_tables()# Create all tables
    add_data()# Upload mock data
    uvicorn.run(app, host="localhost", port=8000) # Start uvicorn
