from fastapi import FastAPI
import uvicorn
import numpy as np
from demographic import plot_joviality_education
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse
from pydantic import BaseModel

app  = FastAPI()

# add homepage
@app.get("/")
def index():
    """Hier shows the homepage message"""
    return "Hello, this is homepage"

@app.get("/rgb")
def rbg():
    rgb_dir = {'18-24':[1.0, 0.7529411764705882, 0.796078431372549],
                '25-31':[0.9411764705882353, 0.5019607843137255, 0.5019607843137255],
                '32-38':[0.803921568627451, 0.3607843137254902, 0.3607843137254902],
                '39-45':[0.6980392156862745, 0.13333333333333333, 0.13333333333333333],
                '46-52':[0.5450980392156862, 0.0, 0.0],
                '53-60':[0.5019607843137255, 0.0, 0.0]}
    return rgb_dir

#@app.post("/login")
#def login():
#    return {"msg": "login successful"}

@app.api_route("/login", methods=("get", "post", "put"))
def login():
    return {"msg": "login successful"}

def square(a):
    return a * a

@app.get("/square_result/{num}")
def square_result(num):
    return {"result of "+ num: square(int(num))}

@app.get("/plot")
def plot():
    plot_joviality_education()
    plot = 'static/joviality_education.png'
    return FileResponse(plot)

class Item(BaseModel):
    num : float


@app.post("/post/")
async def sqrpost(item: Item):
    item_dict = item.dict()
    item_dict.update({"result ":item.num * item.num})
    return item_dict


if __name__ == '__main__':
    uvicorn.run(app)