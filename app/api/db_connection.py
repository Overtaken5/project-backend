import random
import jwt

from fastapi import Form, HTTPException, status, APIRouter
from fastapi.params import Depends
from fastapi.responses import FileResponse
from fastapi.security import HTTPBasic, OAuth2PasswordBearer, OAuth2PasswordRequestForm

from pathlib import Path
from passlib.context import CryptContext
from datetime import timedelta, timezone, datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.api.models.models import Base, Users

auth = APIRouter()
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:sanji@127.0.0.1/service_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base.metadata.create_all(bind=engine)

# создание сессии для БД
SessionLocal = sessionmaker(autoflush=False, bind=engine)
security = HTTPBasic()


# Функция для получения сессии
def get_db():
    db = SessionLocal()  # создаём экземпляр сессии
    try:
        yield db  # возвращаем сессию для использования
    finally:
        db.close()  # закрываем сессию, чтобы освободить ресурсы

SECRET_KEY = "mugiwaraluffy"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15


@auth.get("/")
async def root():
    file_path = Path("app/frontend/index.html")
    return FileResponse(file_path)
