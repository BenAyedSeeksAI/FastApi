import imp
from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()
# def welcome():
#     return 'Hello world'

@app.get("/")
def root():
    data = {"message" : "Welcome to our Api",
    }
    return data

@app.get("/get/posts/")
def getPosts():
    data = {
        "data" : "your posts",
    }
    return data

@app.post("/create/post/")
def createPost(payload: dict = Body(...)):
    print(payload)
    return {"Message" : f"Post created -{payload['title']}- succesfully"}








