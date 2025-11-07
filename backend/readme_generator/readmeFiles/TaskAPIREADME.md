# Task Manager API
================

A RESTful API for managing personal tasks, built with **Django Rest Framework (DRF)** and **JWT authentication**.

This API allows users to register, authenticate, and manage their tasks with filtering, priority levels, and overdue detection.

## Features
------------

- **User Authentication**
  - JWT-based login and token authentication.
  - User registration endpoint with password hashing.

- **Task Management**
  - Create, retrieve, update, and delete tasks.
  - Each task belongs to a specific user.
  - Priority levels (1 = Low, 2 = Medium, 3 = High).
  - Task completion and archival support.

- **Filtering**
  - Filter tasks by:
    - `completed` status
    - `priority`
    - `overdue` (tasks past their due date and not completed).

- **Permissions**
  - Only authenticated users can access task endpoints.
  - Registration is limited to `POST` requests only.

## Tech Stack
--------------

- **Backend:** Django, Django Rest Framework
- **Authentication:** JWT (via `djangorestframework-simplejwt`)
- **Filtering:** django-filter
- **Database:** SQLite (default) or configurable to Postgres/MySQL

## Installation & Setup
------------------------

To set up the Task Manager API, follow these steps:

```bash
git clone https://github.com/benet013/Fullstack-Note-App
cd taskmanagerapi

# create virtual environment
python -m venv venv
source venv/bin/activate   # (on Windows: venv\Scripts\activate)

# install dependencies
pip install -r requirements.txt

# run migrations
python manage.py migrate

# run the server
python manage.py runserver
```

## Endpoints
-------------

| Endpoint | Method | Description |
| --- | --- | --- |
| `/task/` | `GET` | List all tasks |
| `/task/` | `POST` | Create a new task |
| `/task/{id}` | `GET` | Retrieve a task by ID |
| `/task/{id}` | `PUT` | Update a task by ID |
| `/task/{id}` | `DELETE` | Delete a task by ID |
| `/register/` | `POST` | Register a new user |

## API Keys
------------

API keys are used for JWT authentication. You can obtain an API key by registering a new user and logging in.

## Example Use Cases
---------------------

### Register a new user

```bash
curl -X POST \
  http://localhost:8000/register/ \
  -H 'Content-Type: application/json' \
  -d '{"username": "john", "email": "john@example.com", "password": "password"}'
```

### Get all tasks

```bash
curl -X GET \
  http://localhost:8000/task/
```

### Create a new task

```bash
curl -X POST \
  http://localhost:8000/task/ \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{"title": "Buy milk", "description": "Buy milk from the store", "due_date": "2024-03-12T12:00:00", "priority": 2}'
```

### Update a task

```bash
curl -X PUT \
  http://localhost:8000/task/1/ \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{"title": "Buy milk", "description": "Buy milk from the store and bread", "due_date": "2024-03-12T12:00:00", "priority": 2}'
```

### Delete a task

```bash
curl -X DELETE \
  http://localhost:8000/task/1/ \
  -H 'Authorization: Bearer YOUR_API_KEY'
```