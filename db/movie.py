import json
import _sqlite3


def insert_mov(conn,mov):
    cur = conn.cursor()
    cur.execute("INSERT INTO movies VALUES (:name, :imdb_score, :director, :popularity, :genre)",
                {'name': mov['name'], 'director': mov['director'], 'imdb_score': mov['imdb_score'],
                 'popularity': mov['popularity'],'genre': json.dumps(mov['genre'])
                 })


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = _sqlite3.connect(db_file)
        cur = conn.cursor()
    except _sqlite3.Error as e:
        print(e)
    return conn


def get_movies_by_name(conn, name):
    """
    Query movies by title
    :param conn: the Connection object
    :param name: the movie title
    :return: list of movies matching criteria
    """
    cur = conn.cursor()
    cur.execute("SELECT rowid,* FROM movies WHERE name LIKE:name LIMIT 3", {'name': '%' + name + '%'})
    res = cur.fetchall()
    return res


def update_mov(conn, mov):
    cur = conn.cursor()
    cur.execute("""UPDATE movies SET name = :name , director = :director  , imdb_score = :imdb_score ,popularity = :popularity 
                 WHERE rowid = :id""",
                {'name': mov['name'], 'director': mov['director'], 'imdb_score': mov['imdb_score'],
                 'popularity': mov['popularity'], 'id': mov['id']
                 })
    cur.execute("SELECT rowid,* FROM movies WHERE rowid = :id", {'id': mov['id']})
    return cur.fetchall()

def setupUsers(conn,model):
    cur = conn.cursor()
    cur.execute("INSERT INTO users VALUES (:username, :password, :isAdmin)",
                {'username': model['username'], 'password': model['password'], 'isAdmin': model['isAdmin']
                 })
    cur.execute("SELECT * FROM users ")
    return cur.fetchall()


def delete_mov(conn,id):
    cur = conn.cursor()
    cur.execute("Delete from movies where rowid=:id", {'id': id})

def db_main(title='', isInsert=False, isUpdate=False, isDelete=False,model=None):
    database = "movies.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        if isInsert:
            return  insert_mov(conn, model)
        if isUpdate:
            return update_mov(conn, model)
        if isDelete:
            return delete_mov(conn, model)
        return get_movies_by_name(conn, title)

def checkUser(conn, model):
    cur = conn.cursor()
    cur.execute("Select * from users where username=:username AND password=:password", {'username': model['username'], 'password': model['password'] })
    return cur.fetchone()

def db_user(model):
    database = "movies.db"
    # create a database connection
    conn = create_connection(database)
    with conn:
        return checkUser(conn, model)

