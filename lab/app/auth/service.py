from app.auth.security import create_access_token, create_refresh_token

# тимчасова "база користувачів"
fake_users = {
    "admin": {
        "username": "admin",
        "password": "admin"
    }
}


def authenticate(username: str, password: str):
    user = fake_users.get(username)
    if not user or user["password"] != password:
        return None
    return user


def login(username: str):
    return {
        "access_token": create_access_token({"sub": username}),
        "refresh_token": create_refresh_token({"sub": username}),
        "token_type": "bearer"
    }