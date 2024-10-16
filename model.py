from database import get_db
from pymongo.database import Database
from schemas import convo
from typing import Dict
def conversation(db:Database,user:convo)->Dict:
    result={
        "user_input":user.user_input,
        "bot_input":user.bot_input
    }
    res=db["store_convo"].insert_one(result)
    return{
        "ID":str(res.inserted_id),
        "user_input":user.user_input,
        "bot_input":user.bot_input
    }