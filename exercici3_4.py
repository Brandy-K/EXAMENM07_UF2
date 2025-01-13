from fastapi import FastAPI
from pydantic import BaseModel, HTTPException
from dbConnect import get_connection

app = FastAPI()


class UserSchema(BaseModel):
    Name: str
    Surname: str
    Password: str  # Sensible camp
    email: str
    address: str
    CP: int | None = None
    age: int


@app.get("/users", response_model=UserSchema)
async def get_user():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = """
        SELECT * FROM User        
        """
        cursor.execute(query)
        user = cursor.fetchone()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return UserSchema(
            Name=user[0],
            Surname=user[1],
            Password=user[2],
            email=user[3],
            address=user[4],
            CP=user[5],
            age=user[6],
        )
    finally:
        conn.close()
