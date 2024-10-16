from database import get_db
from pymongo.database import Database
from schemas import convo,convo_user
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

def conversation_user(db:Database,user:convo_user):
    result={
       "conversation":user.conversation
    }
    res=db["user_convo"].insert_one(result)
    return{
       "conversation":user.conversation,
       "ID":str(res.inserted_id)
    }