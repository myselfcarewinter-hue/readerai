from jose import jwt


SECRET_KEY = "readerai_secret"
ALGORITHM = "HS256"


def create_access_token(data):

    token = jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token



def decode_token(token):

    data = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    return data