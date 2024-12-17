import random
from fastapi import FastAPI
from api_handler import FastAPIHandler

app = FastAPI()
app.handler = FastAPIHandler()


@app.get("/", tags=['home'])
def home():
    return {"Hello": "World"}

@app.post('/api/prediction')
def make_prediction(car_id: int, item_features: dict):
    prediction = app.handler.predict(item_features)[0]

    
    return ({
             'Present_Price': prediction,
             'car_id': car_id
            })