from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from src.user.schemas import *

user_router = APIRouter()

@user_router.post('/signup', status_code=status.HTTP_202_ACCEPTED)
async def user_signup(auth:UserAuth)->bool:
    