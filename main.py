import json
import optional as optional
from fastapi import FastAPI, Request, Response
from businessLayer.movie import get_movie_json_data, bulk_insert, insertmovie, updatemovie, deletemovie
from typing import Optional
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:3000",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    imdb_score: str
    director: str
    popularity: str
    genre : list
    id: Optional[int] = 0

class RemoveID(BaseModel):
    id: int

@app.get("/")
def home():
    return {"message":"Hello"}

@app.get("/amdb/")
async def getmovie(movietitle: str, request: Request):
    client_host = request.client.host
    return {"client_host": client_host, "result": get_movie_json_data(movietitle)}

@app.post("/amdb/addmovie")
async def addmovie(item: Item):
    data = item.dict()
    insertmovie(data)
    return {"Result":"Success"}

@app.post("/amdb/editmovie")
async def editmovie(item: Item):
    data = item.dict()
    updatemovie(data)
    return {"Result":"Success"}

@app.post("/amdb/removemovie")
async def removemovie(item: RemoveID):
    data = item.dict()
    deletemovie(data['id'])
    return {"Result":"Success"}


@app.get("/amdb/insert")
def read_root():
    return { "result": bulk_insert()}


if __name__ == '__main__':
    """"""



"""uvicorn main: app - -reload"""

