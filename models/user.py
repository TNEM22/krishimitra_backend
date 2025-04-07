from pydantic import BaseModel

class SignupRequest(BaseModel):
  username: str
  display_name: str
  password: str