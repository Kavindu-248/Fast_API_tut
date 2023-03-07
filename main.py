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
    )

]


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}
