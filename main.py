from schemas import convo
from model import conversation
from pymongo.database import Database
from fastapi import FastAPI,Depends
from database import get_db

app=FastAPI()

@app.post("/chat")
async def chat_user_bot(user:convo,db:Database=Depends(get_db)):
    return conversation(db,user)