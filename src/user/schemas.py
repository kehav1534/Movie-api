from pydantic import BaseModel
from typing import Optional

class UserAuth(BaseModel):
    email : str
    pwd : str

class UserInfo(BaseModel):
    email: str
    name: str
    yob : int
    pref_gen : list[str]

class HistoryData(BaseModel):
    mid : str
    wd : float   # watched duration
    
class UserHistory(BaseModel):
    email : str
    data : list[HistoryData]
