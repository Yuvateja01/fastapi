from fastapi import FastAPI,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

from starlette.responses import Response
app = FastAPI()

my_posts = []
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
    return {"data":my_posts}

@app.post("/add-posts",status_code=status.HTTP_201_CREATED)
def addPosts(post:Post):
    post_dict= post.dict()
    post_dict["id"]=randrange(0,10000000)
    my_posts.append(post_dict)
    return {"data":post_dict}

def retreivePost(id):
    for p in my_posts:
        if p["id"]==id:
            return p

def deletePost(id):
    for i,p in enumerate(my_posts):
        if p["id"] == id:
            return i

@app.get("/posts/latest")
def getLatest():
    post = my_posts[len(my_posts)-1]
    return {"data":post}

@app.get("/posts/{id}")
def getPost(id:int):
    post = retreivePost(id)
    if not post:
        raise HTTPException(404,"not found")
   
    return {"post":post}
    
@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delPost(id:int):
    index = deletePost(id)
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

