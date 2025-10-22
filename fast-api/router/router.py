from fastapi import APIRouter,Response, HTTPException
from starlette.status import HTTP_201_CREATED
from schema.user_schema import UserSchema
from config.db import conn,engine
from model.users import users
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import select

user = APIRouter()

@user.get("/")
def read_root():
    return {"Hello": "Mensaje desde router"}

@user.get("/api/user")
def list_users():
    with engine.connect() as conn:
        filas = conn.execute(
            select(users.c.id, users.c.name, users.c.email)  # ¡no expongas password!
        ).mappings().all()  # ← convierte a dict automáticamente
    return filas  # OK: lista de dicts JSON-serializable

@user.get("/api/users/{user_id}")
def get_user(user_id: int):
    with engine.connect() as conn:
        fila = conn.execute(
            select(users.c.id, users.c.name, users.c.email)
            .where(users.c.id == user_id)
        ).mappings().first()
    if not fila:
        raise HTTPException(404, "Usuario no encontrado")
    return fila

@user.post("/api/users", status_code=HTTP_201_CREATED)
def create_user(data_user: UserSchema):
    # Convierte el objeto Pydantic a dict
    user_dict = data_user.model_dump()
    # Hashea la clave antes de guardarla
    user_dict["password"] = generate_password_hash(user_dict["password"])
    with engine.begin() as conn:
        conn.execute(users.insert().values(**user_dict))
    return Response(status_code=HTTP_201_CREATED)


@user.put("/api/users/{user_id}")
def update_user(user_id: int, data_user: UserSchema):
    print(user_id, data_user)