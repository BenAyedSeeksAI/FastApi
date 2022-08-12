import imp
from fastapi import FastAPI

app = FastAPI()
# def welcome():
#     return 'Hello world'

@app.get("/")
def getData():
    data = {"name" : "Fares",
            "age" : "24"
            }
    return data
def HelloWorld():
    return 'Hello world'
def MakeWold():
    return "fares"








