
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Post(BaseModel):
    category: str
    content: str

posts = []

@app.get("/")
def root():
    return {"message": "Routine-log API is running"}

@app.get("/posts")
def get_posts():
    return posts

@app.post("/posts")
def create_post(post: Post):
    data = post.dict()
    data["created_at"] = datetime.now()
    posts.append(data)
    return data



