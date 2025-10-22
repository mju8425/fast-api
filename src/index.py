from fastapi import FastAPI
from router.router import user

app = FastAPI(
    title="FastAPI on Vercel",
    version="1.0.0"
)

# Incluir rutas del router
app.include_router(user)

@app.get("/", tags=["health"])
def home():
    return {"message": "🚀 FastAPI desplegado en Vercel correctamente", "platform": "vercel"}
