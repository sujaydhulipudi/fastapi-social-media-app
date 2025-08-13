import time
from fastapi import FastAPI, Response, HTTPException, status, Depends
from typing import Optional, List
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
import utils
import models, schemas
from database import engine, SessionLocal, get_db
from routers import post, user, auth, vote

models.Base.metadata.create_all(bind=engine)
app = FastAPI()



my_posts=[{"title":"title of post 1", "content": "content of post 1", "id":1}, {"title":"favourite foods", "content":"I like pizza", "id":2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

while True:
    try:
        conn = psycopg2.connect(host='localhost', user='postgres', database='postgres', password='g0disg00d', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Connected to PostgreSQL")
        break
    except Exception as error:
        print("Failed to connect to PostgreSQL")
        print("Error: ", error)
        time.sleep(2)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
@app.get("/")
def index():
    return {"data": 'post-list'}

@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"status": posts}
