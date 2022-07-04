from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
import pymysql


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

#conn = sqlite3.connect('libgen.db', check_same_thread=False)
engine = create_engine('mysql+pymysql://xxxxxx:xxxxxx@localhost/LibGen' )
#connection = mysql.connector.connect(user="dnelub", password="toprakmaya", host="localhost", database="LibGen")
connection = engine.connect()

# define a root `/` endpoint
@app.get("/")
def index():
    #c = connection.cursor()
    results = []
    connection.execute(f"SELECT DISTINCT language, extension FROM books WHERE language IS NOT NULL ")
    columns = [column[0] for column in c.description]
    for row in c.fetchall():
        results.append(dict(zip(columns, row)))
    return results

@app.get("/books")
def index_params(search, keyword, limit, page):
    l=int(limit)
    p=int(page)
    start = l*p
    #c = connection.cursor()
    results = []
    if search=='Title':
        query = connection.execute(f"SELECT * FROM clean_update WHERE Title LIKE '%{keyword}%' ORDER BY ID LIMIT {limit}")
        columns = [column[0] for column in c.description]
        for row in query:
            results.append(dict(zip(columns, row)))
    elif search=='Author':
        c.execute(f"SELECT * FROM books WHERE author LIKE '%{keyword}%' ORDER BY id LIMIT {limit}")
        columns = [column[0] for column in c.description]
        for row in c.fetchall():
            results.append(dict(zip(columns, row)))
    elif search=='Publisher':
        c.execute(f"SELECT * FROM books WHERE publisher LIKE '%{keyword}%' ORDER BY id LIMIT {limit}")
        columns = [column[0] for column in c.description]
        for row in c.fetchall():
            results.append(dict(zip(columns, row)))
    return results
