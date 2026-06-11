import jwt
from fastapi import HTTPException , status, Request
from src.user.dtos import UserSchema , LoginSchema
from sqlalchemy.orm import Session
from src.user.models import UserModel
from pwdlib import PasswordHash
from datetime import datetime , timedelta
from jwt.exceptions import InvalidTokenError
from src.utils.settings import setting
from src.utils.mail import send_email

password_hash = PasswordHash.recommended() #create object for passwordhash

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


async def register(body:  UserSchema, db : Session):
    ## 1. check duplicate username
    is_user = db.query(UserModel).filter(UserModel.username == body.username).first() ## first object do
    if is_user:
        raise HTTPException(status_code=400, detail="User already exists")

    ##2. email also unique
    is_user = db.query(UserModel).filter(UserModel.email == body.email).first()
    if is_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    #store -> encrypt
    hashed_password = get_password_hash(body.password)
    new_user = UserModel(
        name=body.name,
        username=body.username,
        hash_password = hashed_password,
        email=body.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    ## send email confirmation
    res = await send_email([new_user.email])
    print(res)
    return new_user


def login_user(body : LoginSchema, db : Session):
    user = db.query(UserModel).filter(UserModel.username == body.username).first() ## first object do
    if not user:
        raise HTTPException(status_code=401, detail="Username not exists")

    if not verify_password(body.password, user.hash_password):
        raise HTTPException(status_code=401, detail="Incorrect Password")

    #both correct now generate token
    exp_time = datetime.now() + timedelta(minutes=setting.EXP_TIME)
    token = jwt.encode({"_id" : user.id , "exp" : exp_time.timestamp()},setting.SECRET_KEY,setting.ALGORITHM)

    return{"token" : token}


# api ko call karenge toh token use krenge ---> toh sent token using header

def is_authenticated(request : Request , db: Session):
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