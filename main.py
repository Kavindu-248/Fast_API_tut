from fastapi import FastAPI
from models import User, Gender, Role
from typing import List
from uuid import uuid4


app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="John",
        last_name="Doe",
        gender=Gender.male,
        roles=[Role.student]
    ),

    User(
        id=uuid4(),
        first_name="Jane",
        last_name="Jackson",
        gender=Gender.female,
        roles=[Role.admin, Role.user]
    ),



]


@app.get("/")
async def root():
    return {"Hello": "World"}
