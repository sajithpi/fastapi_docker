from fastapi import Form
from pydantic import BaseModel
class Post(BaseModel):
    title:str
    description:str
    user_id:int
    
    @classmethod
    def as_form(
        cls,
        title: str = Form(...),
        description: str = Form(...),
        user_id: int = Form(...)
    ):
        return cls(
            title=title,
            description=description,
            user_id=user_id
        )
class Users(BaseModel):
    username:str
    email:str
    sponser_id:int
    adrs : str
    
    @classmethod
    def as_form(
        cls,
        username:str = Form(...),
        email:str = Form(...),
        sponser_id:int = Form(...),
        adrs : str = Form(...)
    ):
        return cls(
            username=username,email=email,sponser_id=sponser_id,adrs=adrs
        )