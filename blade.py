from random import randrange
from fastapi import FastAPI
from fastapi.params import Body
from model import Post

app = FastAPI()
all_posts = []
@app.get("/")
def root():
    data = {"message" : "Welcome to our Api",
    }
    return data

@app.get("/get/posts/")
def getPosts():
    data = {
        "data" : all_posts,
    }
    return data

@app.post("/create/post/")
def createPost(post: Post):
    post = post.dict()
    post["id"] = randrange(0,1000000)
    all_posts.append(post)
    return {"Message" : "Post created succesfully"}
