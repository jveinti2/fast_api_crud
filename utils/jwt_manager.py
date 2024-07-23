from jwt import encode, decode

def create_token(data: dict, secret: str):
    return encode(data, secret, algorithm='HS256')

def validate_token(token: str, secret: str):
    data: dict = decode(token, secret, algorithms=['HS256'])
    return data