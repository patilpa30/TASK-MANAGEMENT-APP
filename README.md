# 🚀 Task Management API

A RESTful Task Management Application built with FastAPI, PostgreSQL, SQLAlchemy, and JWT Authentication.

This project allows users to register, login, and manage their personal tasks securely. Each user can create, update, view, and delete only their own tasks.

---

## ✨ Features

### 👤 User Management
- User Registration
- User Login
- JWT Token Authentication
- Password Hashing using pwdlib
- User Authorization Middleware
- Registration Email Confirmation

### ✅ Task Management
- Create Task
- Get All User Tasks
- Get Single Task
- Update Task
- Delete Task
- Task Ownership Validation

### 🔐 Security
- Passwords are stored in hashed format
- JWT based authentication
- Protected APIs using FastAPI Dependencies
- Users can only access their own tasks

### 🗄 Database
- PostgreSQL
- SQLAlchemy ORM
- Alembic Migration Support

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| FastAPI | Backend Framework |
| PostgreSQL | Database |
| SQLAlchemy | ORM |
| Alembic | Database Migration |
| JWT | Authentication |
| Pydantic | Data Validation |
| FastAPI Mail | Email Service |
| pwdlib | Password Hashing |

---

# 📂 Project Structure

```text
TASK_MANAGEMENT_APP
│
├── migrations/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── src/
│   ├── tasks/
│   │   ├── controller.py
│   │   ├── dtos.py
│   │   ├── models.py
│   │   └── router.py
│   │
│   ├── user/
│   │   ├── controller.py
│   │   ├── dtos.py
│   │   ├── models.py
│   │   └── router.py
│   │
│   └── utils/
│       ├── db.py
│       ├── helpers.py
│       ├── mail.py
│       └── settings.py
│
├── .env
├── alembic.ini
├── main.py
└── requirements.txt
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/task-management-api.git

cd task-management-api
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create `.env`

```env
DB_CONNECTION=postgresql://postgres:postgres@localhost:5432/postgres

SECRET_KEY=your_secret_key

ALGORITHM=HS256

EXP_TIME=30
```

---

# 🗄 Database Migration

Initialize Alembic

```bash
alembic init migrations
```

Create Migration

```bash
alembic revision --autogenerate -m "initial migration"
```

Apply Migration

```bash
alembic upgrade head
```

---

# ▶️ Run Application

```bash
uvicorn main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

Redoc:

```text
http://127.0.0.1:8000/redoc
```

---

# 🔑 Authentication Flow

### Register User

```http
POST /user/register
```

Request Body

```json
{
  "name": "Priti",
  "username": "priti",
  "password": "password123",
  "email": "priti@gmail.com"
}
```

---

### Login User

```http
POST /user/login
```

Request

```json
{
  "username": "priti",
  "password": "password123"
}
```

Response

```json
{
  "token": "JWT_TOKEN"
}
```

---

### Verify Authentication

```http
GET /user/is_auth
```

Header

```text
Authorization: Bearer JWT_TOKEN
```

---

# ✅ Task APIs

All Task APIs require JWT Authentication.

Header

```text
Authorization: Bearer JWT_TOKEN
```

---

## Create Task

```http
POST /tasks/create
```

Request

```json
{
  "title": "Learn FastAPI",
  "description": "Complete JWT Authentication",
  "is_completed": false
}
```

---

## Get All Tasks

```http
GET /tasks/all_tasks
```

---

## Get One Task

```http
GET /tasks/one_task/{task_id}
```

Example

```http
GET /tasks/one_task/1
```

---

## Update Task

```http
PUT /tasks/update_task/{task_id}
```

Request

```json
{
  "title": "Updated Title",
  "description": "Updated Description",
  "is_completed": true
}
```

---

## Delete Task

```http
DELETE /tasks/delete_task/{task_id}
```

---

# 📧 Email Service

After successful registration:

- Confirmation email is sent
- SMTP configured using Gmail
- Implemented using FastAPI-Mail

---

# 🔒 Authorization Logic

Each task is linked to a specific user.

```python
TaskModel.user_id
```

Checks performed:

- User must be authenticated
- User can update only their tasks
- User can delete only their tasks
- User cannot access another user's task data

---

# 📊 Current Implemented Modules

### User Module

- Registration
- Login
- JWT Authentication
- Password Hashing
- Email Confirmation

### Task Module

- Create Task
- Read Task
- Update Task
- Delete Task
- Ownership Validation

---

# 🚧 Future Improvements

- Refresh Tokens
- Forgot Password
- Email Verification
- Role Based Access Control (RBAC)
- Pagination
- Search & Filters
- Task Categories
- Due Dates
- Docker Support
- CI/CD Pipeline
- Unit Testing
- Redis Caching

---

# 👨‍💻 Author

Priti Patil

Built using FastAPI, PostgreSQL and SQLAlchemy.
