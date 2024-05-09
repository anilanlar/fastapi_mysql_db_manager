from fastapi import FastAPI, HTTPException
import uvicorn
from database import create_tables
from query import *
from model import *


app = FastAPI()


@app.post("/db-manager-login/", response_model= str)
def add_user(db_manager: DBManager):
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

 
@app.post("/add-user/", response_model= str)
def add_user(user: User):
    try:
        # add_new_user(user.username, user.password)
        return "User added successfully"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    create_tables()
    uvicorn.run(app, host="localhost", port=8000)
