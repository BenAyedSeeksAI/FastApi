from random import randrange
from fastapi import FastAPI
from fastapi.params import Body
from model import Post

app = FastAPI()

all_posts = [{
    "id" : 5,
    "title" : "From Zero to Hero",
    "content": "start from scratch and don't depend on anyone!!",
    "published" : True,
    "rating" : 7
},]

def findPost(id,all_posts):
    ans = None
    for pst in all_posts:
        if pst["id"] == id:
            ans = pst
            break
    return ans

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

@app.get("/get/posts/{post_id}/")
def getPostId(post_id : int):
    global all_posts
    post = findPost(post_id, all_posts)
    return {"detailed post" : post}


@app.post("/create/post/")
def createPost(post: Post):
    post = post.dict()
    post["id"] = randrange(0,1000000)
    all_posts.append(post)
    return {"Message" : "Post created succesfully"}