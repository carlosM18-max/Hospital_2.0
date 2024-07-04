from fastapi import FastAPI
from routes.person import person
from routes.user import user
from routes.users import user

app = FastAPI()  # variable app
app.include_router(person)  # Luego agrega las rutas
# app.include_router(user)
app.include_router(user)

print("Bienvenido al servidor uvicorn")