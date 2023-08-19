from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return {"message": "Você gerou um novo item!"}, item

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep learning FTW!"}
    
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}



@app.get("/accountID={account123ID}&secretKey={secret123Key}")
async def read_item(account123ID:int,secret123Key:int):
    return {"accountID": account123ID,
            "secretKey": secret123Key,
            "message": "Hello World"}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "The current user"}


@app.get("/users/{user_id}")
async def read_user(user_id:str):
    return {"user_id": user_id}

@app.get("/apisharp/")
async def read_query(accountID:int, secretKey:int):
    return {"accountID": accountID, "secretKey": secretKey}