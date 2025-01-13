from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dbConnect import get_connection

app = FastAPI()


class User(BaseModel):
    nombre: str
    apellido: str
    correoelectronico: str
    descripcion: str | None = None
    curso: str
    año: int
    direccion: str
    codigopostal: int | None = None
    userpassword: str


@app.post("/User")
async def add_user(user: User):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = """
        INSERT INTO usuari (Nombre, Apellido, correoelectronico, Descripcion, Curso, Año, Direccio, CodigoPostal, Password)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            user.nombre,
            user.apellido,
            user.correoElectronico,
            user.descripcion,
            user.curso,
            user.año,
            user.direccio,
            user.codigopostal,
            user.userpassword
        ))
        conn.commit()
        return {"message": "User added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    finally:
        conn.close()



