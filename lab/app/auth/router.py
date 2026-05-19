from flask import request
from flask_restful import Resource

from app.auth.service import authenticate, login
from app.auth.security import decode_token, create_access_token


class LoginResource(Resource):

    def post(self):
        data = request.get_json()

        user = authenticate(
            data.get("username"),
            data.get("password")
        )

        if not user:
            return {"message": "Invalid credentials"}, 401

        return login(user["username"])


class RefreshResource(Resource):

    def post(self):
        data = request.get_json()
        token = data.get("refresh_token")

        try:
            payload = decode_token(token)

            if payload.get("type") != "refresh":
                return {"message": "Invalid token type"}, 401

            new_access = create_access_token({
                "sub": payload["sub"]
            })

            return {"access_token": new_access}

        except Exception:
            return {"message": "Invalid token"}, 401