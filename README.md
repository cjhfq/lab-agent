# lab-agent

实验室管理系统的前后端分离实践项目：后端基于 FastAPI + SQLAlchemy + MySQL，前端基于 Vue 3 + Vite + Element Plus，实现用户注册、登录（JWT 鉴权）及实验室/设备等基础页面。

## 技术栈

| 端 | 技术 |
| --- | --- |
| 后端 | Python 3.13、FastAPI 0.115、SQLAlchemy 2.0、PyMySQL、PyJWT、bcrypt、pydantic-settings |
| 前端 | Vue 3.5、Vite 8、Element Plus、axios、vue-router |

## 目录结构

```
lab-agent/
├── backend/                 # FastAPI 后端
│   ├── app/
│   │   ├── api/             # 路由：auth（注册/登录）、user
│   │   ├── common/          # 统一响应体与异常处理
│   │   ├── dependencies/    # 依赖注入（当前登录用户）
│   │   ├── models/          # SQLAlchemy 模型
│   │   ├── schemas/         # Pydantic 请求/响应模型
│   │   ├── utils/           # JWT、密码哈希
│   │   ├── config.py        # 读取 .env 的配置
│   │   ├── database.py      # 引擎与会话
│   │   └── main.py          # 应用入口、CORS、异常注册
│   ├── .env.example         # 环境变量示例
│   └── requirement.txt      # 依赖清单
└── frontend/                # Vue 3 前端
    ├── src/
    │   ├── api/             # 接口封装
    │   ├── utils/           # axios 实例、token 与用户信息处理
    │   ├── layouts/         # 布局
    │   ├── router/          # 路由与守卫
    │   └── views/           # 登录、注册、首页、用户、实验室、设备
    └── .env.development.example
```

## 环境要求

- Python 3.13+
- Node.js ^22.18.0 或 >=24.12.0
- MySQL 5.7+/8.0，需提前创建数据库（默认库名 `lab_agent`）

## 后端启动

```bash
cd backend
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirement.txt
```

创建配置文件（Windows 用 `copy` 代替 `cp`）：

```bash
cp .env.example .env
```

编辑 `.env`，至少填好 `DATABASE_URL` 与 `JWT_SECRET_KEY`：

```dotenv
DATABASE_URL=mysql+pymysql://user:password@localhost:3306/lab_agent
JWT_SECRET_KEY=请替换为随机长字符串
JWT_EXPIRE_HOURS=24
JWT_ALGORITHM=HS256
```

启动服务（表结构通过 `Base.metadata.create_all()` 自动创建）：

```bash
uvicorn app.main:app --reload
```

- 服务地址：<http://localhost:8000>
- 接口统一前缀：`/api`
- 交互式文档：<http://localhost:8000/docs>

## 前端启动

```bash
cd frontend
npm install
cp .env.development.example .env.development
npm run dev
```

- 开发地址：<http://localhost:5173>
- `.env.development` 中的 `VITE_API_BASE_URL` 指向后端地址，默认 `http://localhost:8000`
- 后端 CORS 白名单为 `localhost:5173` 与 `127.0.0.1:5173`，如改端口需同步修改 `backend/app/main.py`

打包：

```bash
npm run build
```

## 安全提示

仓库中**不包含**任何真实 `.env` 文件。请勿把数据库密码、`JWT_SECRET_KEY` 等提交到版本库，本地配置仅保留在 `.env` / `.env.development` 中（均已在 `.gitignore` 中忽略）。
