from jwt import encode, decode

def solicita_token(dato: dict) -> str:
    token: str = encode(payload=dato, key='TYPE-ORT-MERCURY', algorithm='HS256')
    return token

def valida_token(token: str) -> dict:
    dato: dict = decode(token, key='TYPE-ORT-MERCURY', algorithms=['HS256'])
    return dato
