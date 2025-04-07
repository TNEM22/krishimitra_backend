import httpx
import os
from dotenv import load_dotenv

load_dotenv()

VOX_ACCOUNT_ID = os.getenv("VOXIMPLANT_ACCOUNT_ID")
VOX_API_KEY = os.getenv("VOXIMPLANT_API_KEY")
VOX_APP_ID = os.getenv("VOXIMPLANT_APP_ID")
VOX_API_URL = "https://api.voximplant.com/platform_api/"


async def create_voximplant_user(username: str, display_name: str, password: str) -> bool:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            VOX_API_URL + 'AddUser/',
            data={
                "account_id": VOX_ACCOUNT_ID,
                "api_key": VOX_API_KEY,
                "user_name": username,
                "user_display_name": display_name,
                "user_password": password,
                "application_id": VOX_APP_ID
            },
        )
        # print(response.json())
        return response.status_code == 200 and response.json().get("result")


async def get_online_users():
    async with httpx.AsyncClient() as client:
        response = await client.get(VOX_API_URL + 'GetUsers/', params={
            "account_id": VOX_ACCOUNT_ID,
            "api_key": VOX_API_KEY,
            "application_id": VOX_APP_ID,
        })
        print(response.json())
        if response.status_code != 200:
            return []

        data = response.json()
        return data.get("result", [])
