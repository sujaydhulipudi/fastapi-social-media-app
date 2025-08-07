# FastAPI Social Media App 🚀

This is a fully functional backend API for a social media application, built with [FastAPI](https://fastapi.tiangolo.com/) and PostgreSQL, following the [FreeCodeCamp.org Python API Development Course](https://www.youtube.com/watch?v=0sOvCWFmrtA).

## 🔧 Features

- User registration and login with JWT authentication
- Create, read, update, delete (CRUD) operations for posts
- Vote (like/unlike) functionality
- PostgreSQL integration using SQLAlchemy ORM
- Password hashing with bcrypt
- Data validation using Pydantic
- RESTful routing structure
- Alembic for database migrations

## 📦 Tech Stack

- Python 3.11+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- Uvicorn
- JWT (Python-Jose)
- Bcrypt

## 🚀 Getting Started

### Prerequisites

- Python installed
- PostgreSQL installed and running
- Create a `.env` file with your DB credentials and secret key

### Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/fastapi-social-media-app.git
cd fastapi-social-media-app

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
alembic upgrade head

# Start the server
uvicorn app.main:app --reload
