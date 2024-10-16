from pydantic import BaseModel
class convo(BaseModel):
    user_input:str
    bot_input:str

class convo_user(BaseModel):
    user_input:str
    bot_input:str