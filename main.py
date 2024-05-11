from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

import uvicorn
from database import create_tables
from query import *
from model import *

app = FastAPI()

@app.post("/db-manager-login/", response_model= str)
def db_manager_login(db_manager: DBManager):
    try:
        if db_manager_login(db_manager.username, db_manager.password):
            return "DB LOGIN SUCCESS"
        else:
            raise HTTPException(status_code=401, detail="Invalid credentials")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/change-stadium-name/", response_model=str)
def change_stadium_name(dct: dict):
    try:
        if update_stadium_name(dct["old_name"], dct["new_name"]):
            return "Stadium name updated successfully"
        else:
            raise HTTPException(status_code=404, detail="Stadium not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/delete-match-session/", response_model=str)
def delete_match_session(session: DeleteSessionRequest):

    sId= session.session_id
    num_of_deleted_rows = delete_match_session_query(sId)
    if num_of_deleted_rows > 0:
        return "Match session deleted successfully >>> " + str(num_of_deleted_rows)+ " rows affected"
    else:
        return HTTPException(status_code=404, detail="Session not found")
    
@app.post("/add-match-session/", response_model=str)
def add_match_session(match_session: AddMatchSession):
    try:
        add_match_session_query(match_session.coach_username, match_session.stadium_id, match_session.time_slot, match_session.date, match_session.jury_name, match_session.jury_surname)
        return "Match session added successfully"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
    
# @app.get("/get-stadiums", response_model=list)
# def get_stadiums():
#     try:
#         stadiums = get_stadiums_query()
#         return stadiums
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
@app.get("/get-stadiums")
def get_stadiums():
    try:
        stadiums = get_stadiums_query()
        jsonResponse = {}
        for i in range(len(stadiums)):
            jsonResponse[i] = stadiums[i]
        return JSONResponse(content=jsonResponse)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


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
@app.post("/add-new-user/", response_model=str)
def add_new_user(user: AddUserRequest):
    try:
        add_new_user_query(user.user_type, user.username, user.password, user.name, user.surname, user.date_of_birth, user.height, user.weight, user.nationality)
        return "User added successfully"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    


if __name__ == "__main__":
    create_tables()
    uvicorn.run(app, host="localhost", port=8000)
