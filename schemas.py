from pydantic import BaseModel
from typing import List,Dict
class convo(BaseModel):
    user_input:str
    bot_input:str

class convo_user(BaseModel):
    conversation:List[Dict[str, str]]