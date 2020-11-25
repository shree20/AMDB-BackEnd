from fastapi import FastAPI, Request
from businessLayer.movie import get_movie_json_data, insertmovie, updatemovie, deletemovie,get_user_json_data
from fastapi.middleware.cors import CORSMiddleware
from model import movie, users

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message":"Test API"}

@app.get("/amdb/")
async def getmovie(movietitle: str, request: Request):
    client_host = request.client.host
    return {"client_host": client_host, "result": get_movie_json_data(movietitle)}

@app.post("/amdb/addmovie")
async def addmovie(item: movie.Movie):
    data = item.dict()
    insertmovie(data)
    return {"Result":"Success"}

@app.post("/amdb/editmovie")
async def editmovie(item: movie.Movie):
    data = item.dict()
    updatemovie(data)
    return {"Result":"Success"}

@app.post("/amdb/removemovie")
async def removemovie(item: movie.RemoveMovie):
    data = item.dict()
    deletemovie(data['id'])
    return {"Result":"Success"}


@app.post("/amdb/isuser")
async def isUser(item: users.User):
    data = item.dict()
    resp = get_user_json_data(data)
    return {"Result":resp}


if __name__ == '__main__':
    """"""



"""uvicorn main: app --reload"""

