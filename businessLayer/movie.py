
from db.movie import db_main, insert_mov, db_user


def get_movie_json_data(movietitle):
    results = db_main(movietitle)
    jsonresult = []
    for result in results:
        dicts = {
                 'id': result[0],
                 'title': result[1],
                 'imdb_score': result[2],
                 'director': result[3],
                 'popularity': result[4],
                 'genre': result[5]
                }
        jsonresult.append(dicts)
    return jsonresult


def get_user_json_data(model):
    result = db_user(model)
    if result:
        dict = {
            'username': result[0],
            'password': result[1],
            'isAdmin': result[2],
        }
        return dict
    return None

def insertmovie(model):
    db_main('',True,False,False, model)

def updatemovie(model):
    return db_main('',False,True,False, model)

def deletemovie(id):
    return db_main('', False, False, True, id)

def isuser(model):
    return db_user(model)


