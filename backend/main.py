from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Render Root Directory = backend 이므로 templates 폴더는 backend/templates
templates = Jinja2Templates(directory="templates")


class Post(BaseModel):
    category: str
    content: str


posts = []


# API 상태 확인 (JSON)
@app.get("/")
def root():
    return {"message": "Routine-log API is running"}


# UI 화면 (HTML) - 여기로 접속: /ui
@app.get("/ui", response_class=HTMLResponse)
def ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# API: 전체 글 조회
@app.get("/posts")
def get_posts():
    return posts


# API: 글 생성
@app.post("/posts")
def create_post(post: Post):
    data = post.dict()
    # datetime은 JSON으로 바로 못 나가서 문자열로 저장
    data["created_at"] = datetime.now().isoformat()
    posts.append(data)
    return data


