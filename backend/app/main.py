from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from app.database import engine, Base
from app.models.user import User
from app.api import api
from fastapi.middleware.cors import CORSMiddleware
from app.common.exceptions import (
    BusinessException,
    business_exception_handler,
    global_exception_handler,
    http_exception_handler,
    validation_exception_handler,
)

Base.metadata.create_all(bind=engine)  # 自动创建数据库表

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 允许前端源，不要直接写"["*"]"
    allow_credentials=True,  # 关键，允许前端携带Authorization token
    allow_methods=["*"],  # 允许所有请求方法 get post delete put options
    allow_headers=["*"],  # 允许所有请求头，包括Authorization
)
app.include_router(api)
# 注册异常处理器
app.add_exception_handler(BusinessException, business_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
# 兜底异常处理器
app.add_exception_handler(Exception, global_exception_handler)


@app.get("/")
def getRoot():
    return {"message": "hello fastapi"}
