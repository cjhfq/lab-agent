from app.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"comment": "用户信息表"}

    username: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False, comment="用户名"
    )
    password: Mapped[str] = mapped_column(String(50), nullable=False, comment="密码")
    name: Mapped[str] = mapped_column(String(50), nullable=False, comment="姓名")
    role: Mapped[str] = mapped_column(
        String(20), nullable=False, comment="角色：student-学生，admin-管理员"
    )
    email: Mapped[str | None] = mapped_column(String(50), comment="邮箱")
    phone: Mapped[str | None] = mapped_column(String(20), comment="手机号")
    avatar: Mapped[str | None] = mapped_column(String(50), comment="头像")
    status: Mapped[int] = mapped_column(default=1, comment="状态：0-禁用，1-启用")
