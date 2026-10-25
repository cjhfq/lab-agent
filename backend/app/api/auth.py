from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.common.exceptions import BusinessException
from app.common.response import Response
from app.database import get_db

from app.schemas.auth import LoginRequest, LoginResponce
from app.models.user import User
from app.schemas.user import UserResponse
from app.utils.password import verify_password
from app.utils.jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["权限验证接口"])


@router.post("/login")
def login(data: LoginRequest, session: Session = Depends(get_db)):
    # 根据用户账号登录
    user = session.query(User).filter(User.username == data.username).first()
    # 校验账号是否正确
    if not user or not verify_password(data.password, user.password):
        raise BusinessException("账号或密码错误")
    # 校验用户状态
    if user.status != 1:
        raise BusinessException("账号已被禁用")
    # 创建token
    token = create_access_token(user.id)
    return Response.success(
        message="登录成功",
        data=LoginResponce(
            token=token,
            user=UserResponse.model_validate(user),
        ),
    )
