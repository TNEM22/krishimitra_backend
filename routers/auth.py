from fastapi import APIRouter, HTTPException
from models.user import SignupRequest
from services.voximplant_service import create_voximplant_user, get_online_users

router = APIRouter()


@router.post('/signup')
async def signup(request: SignupRequest):
    success = await create_voximplant_user(request.username, request.display_name, request.password)
    # print(success)
    if not success:
        raise HTTPException(status_code=400, detail="Fail to create user.")
    return {"message": "User created successfully"}


@router.get('/users/online')
async def users():
    res = await get_online_users()
    return {"data": res}
