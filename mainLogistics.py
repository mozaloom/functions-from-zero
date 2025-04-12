from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from mylib.logistics import find_distance, list_cities, travel_time


app = FastAPI()


class City(BaseModel):
    city1: str
    city2: str
    # default speed


@app.get("/")
async def root():
    """Home Page with GET HTTP Method"""

    return {"message": "Hello FastAPI Logistics"}


@app.get("/cities")
async def cities():
    """Cities Page with GET HTTP Method"""
    return {"cities": list_cities()}


@app.post("/distance")
# distance between two cities
async def distance(city: City):
    """Distance Page with POST HTTP Method

    example usage:
    curl -X POST "http://localhost:8080/distance" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"city1\":\"New York\", \"city2\":\"Los Angeles\"}"


    """
    result = find_distance(city.city1, city.city2)
    if result is None:
        return {"error": "City not found"}
    return {"distance": result}


@app.post("/travel_time")
# travel time between two cities given a speed
async def travel_time_endpoint(city: City):
    """Travel Time Page with POST HTTP Method

    example usage:
    curl -X POST "http://localhost:8080/travel_time" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"city1\":\"New York\", \"city2\":\"Los Angeles\", \"speed\":60}"


    """
    result = travel_time(city.city1, city.city2)
    if result is None:
        return {"error": "City not found"}
    return {"travel_time": result}


if __name__ == "__main__":

    uvicorn.run(app, port=8080, host="0.0.0.0")
