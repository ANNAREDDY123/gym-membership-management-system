# gym-membership-management-system
Gym Membership Management System built with FastAPI, SQLAlchemy, Pydantic, SQLite, and JWT Authentication for managing members, trainers, subscriptions, and trainer assignments.
gym-membership-management-system-main
│
├── auth
│   └── auth_handler.py
│
├── models
│   ├── user.py
│   ├── member.py
│   ├── trainer.py
│   └── subscription.py
│
├── schemas
│   ├── user.py
│   ├── member.py
│   ├── trainer.py
│   └── subscription.py
│
├── routers
│   ├── auth.py
│   ├── member.py
│   ├── trainer.py
│   └── subscription.py
│
├── sql
│   └── schema.sql
│
├── database.py
├── main.py
├── requirements.txt
└── README.md

# Gym Membership Management System

## Features

- JWT Authentication
- Member Management
- Trainer Management
- Subscription Management
- Trainer Assignment
- SQLite Database
- Swagger Documentation

## APIs

### Authentication
- POST /auth/register
- POST /auth/login

### Members
- POST /members
- GET /members
- GET /members/{id}
- PUT /members/{id}
- DELETE /members/{id}

### Trainers
- POST /trainers
- GET /trainers
- PUT /trainers/{id}
- DELETE /trainers/{id}

### Subscriptions
- POST /subscriptions
- GET /subscriptions
- GET /subscriptions/{id}

### Trainer Assignment
- POST /trainers/{trainer_id}/members/{member_id}
- GET /trainers/{trainer_id}/members


