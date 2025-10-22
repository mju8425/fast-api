from fastapi import APIRouter

user = APIRouter(prefix="", tags=["users"])

@user.get("/users")
def list_users():
    # Ejemplo simple
    return {"users": ["Juan", "Ana", "Pedro"]}
