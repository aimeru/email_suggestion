from pydantic import BaseModel

class AiResponse(BaseModel):
    Response1: str
    Response2: str