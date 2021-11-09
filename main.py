from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title:str
    author:str
    published:bool = True
    rating:Optional[int] = None

@app.get("/")
def sendMessage():
    return {"message": "Dev is copium"}

@app.get("/posts")
def getPosts():
    return {"data":"all posts here"}

@app.post("/add-posts")
def addPosts(post:Post):
    print(post)
    return {"title":post.title, "author":post.author}