from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import add_new_user
from main import app

# Assuming add_new_user function is defined elsewhere

class User(BaseModel):
    username: str
    password: str

@app.post("/add-user/", response_model= str)
def add_user(user: User):
    try:
        add_new_user(user.username, user.password)
        return {"message": "User added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
