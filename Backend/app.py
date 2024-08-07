from fastapi import FastAPI
from routes.persons import person
from routes.users import user
from routes.roles import rol
from routes.users_roles import users_roles
from routes.solicitudes import request

app = FastAPI()  # variable app
app.include_router(person)  # Luego agrega las rutas
# app.include_router(user)
app.include_router(user)
app.include_router(rol)
app.include_router(users_roles)
app.include_router(request)

print("Bienvenido al servidor uvicorn")