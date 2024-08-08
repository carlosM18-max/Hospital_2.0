from fastapi import FastAPI
from routes.user import user
from routes.person import person
from routes.rol import rol
from routes.userrol import userrol
from routes.tbc_organos import tbc_organos  # Importar el enrutador de organos

app = FastAPI()  # variable app
app.include_router(person)  # Luego agrega las rutas
app.include_router(user)
app.include_router(rol)
app.include_router(userrol)
app.include_router(tbc_organos)  # Agregar el enrutador de organos

print("Bienvenido al servidor uvicorn")
