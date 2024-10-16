from schemas import convo
from model import conversation
from pymongo.database import Database
from fastapi import FastAPI,Depends
from database import get_db
import os
import uvicorn

app=FastAPI()

@app.post("/chat")
async def chat_user_bot(user:convo,db:Database=Depends(get_db)):
    return conversation(db,user)

@app.get("/get_prod_det")
async def get_prod_det(user:convo,db:Database=Depends(get_db)):
    result = list(db["store_convo"].find({}))  # Convert cursor to list
    # Convert MongoDB documents (which are BSON) into JSON serializable objects
    return {"conversations": [dict(item) for item in result]}
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Get port from env or use 8000 as default
    uvicorn.run(app, host="0.0.0.0", port=port)