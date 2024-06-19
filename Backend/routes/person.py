from fastapi import APIRouter

person = APIRouter()

@person.get("/person")

def helloworld():
    return "Hello world"