from datetime import timedelta
from app.core.security import hash_password, verify_password, create_token
from app.db.mongo import users_collection
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_DAYS

class AuthService:

    async def register(self, user):
        user_dict = {
            "username": user.username,
            "password": hash_password(user.password)
        }
        await users_collection.insert_one(user_dict)
        return True

    async def login(self, form_data):
        
        db_user = await users_collection.find_one(
            {"username": form_data.username}
        )
        print(form_data.username)
        print(form_data.password)
        print(db_user)
        if not db_user or not verify_password(
            form_data.password,
            db_user["password"]
        ):
            return {"error": "Invalid credentials"}

        access = create_token(
            {"sub": form_data.username},
            timedelta(minutes=30)
        )

        refresh = create_token(
            {"sub": form_data.username, "type": "refresh"},
            timedelta(days=7)
        )

        return {
            "access_token": access,
            "refresh_token": refresh,
            "token_type": "bearer"
        }