from fastapi import FastAPI
from routes.person import person

app = FastAPI()  # variable app
app.include_router(person)  # Luego agrega las rutas

print("Bienvenido al servidor uvicorn")