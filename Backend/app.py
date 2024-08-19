from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.persons import person
from routes.users import user
from routes.roles import rol
from routes.users_roles import users_roles
from routes.solicitudes import request
from routes.tbc_organos import tbc_organos  
from routes.personal_medico import personal_medico
from routes.departamentos import departamentos
from routes.areas_medicas import area_medica
from routes.servicios_medicos import serviceM


app = FastAPI()  # variable app

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

app.include_router(person)  # Luego agrega las rutas
app.include_router(user)
app.include_router(personal_medico)
app.include_router(area_medica)
app.include_router(departamentos)
app.include_router(rol)
app.include_router(users_roles)
app.include_router(request)
app.include_router(tbc_organos)
app.include_router(serviceM)




print("Bienvenido al servidor uvicorn")