from fastapi import HTTPException, status, Request
from fastapi.params import Depends
from src.utils.settings import setting
from sqlalchemy.orm import Session
import jwt
from jwt.exceptions import InvalidTokenError
from src.user.models import UserModel
from src.utils.db import get_db


# api ko call karenge toh token use krenge ---> toh sent token using header
#use this function as dependency function
def is_authenticated(request : Request , db: Session= Depends(get_db)):
    try:
        token = request.headers.get("authorization")
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized")

        token = token.split(" ")[-1]

        data = jwt.decode(token,setting.SECRET_KEY , setting.ALGORITHM)
        user_id = data.get("_id")

        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            raise HTTPException(status_code=401, detail="You are Unauthorized")

        return user
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="You are Unauthorized")