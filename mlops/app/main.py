from fastapi import FastAPI

from app.models import House
from app.services import HousePrices

app = FastAPI()

house_prices = HousePrices()
house_prices.load_model()

@app.get("/")
def home():
    return {"First": "API"}

@app.post("/predict")
def predict(house: House) -> float:
    return house_prices.predict(house)
