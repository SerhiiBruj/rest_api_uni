from flask import request
from app.auth.security import decode_token


def get_current_user():
    auth = request.headers.get("Authorization")

    if not auth:
        return None

    try:
        token = auth.split(" ")[1]
        payload = decode_token(token)

        if payload.get("type") != "access":
            return None

        return payload.get("sub")

    except Exception:
        return None