# LGApi_ORM
API server for Library Genesis (LG) Database by using Object-Relational Mapping (ORM)

## Packages
* Python
* FastAPI
* SQLAlchemy
* Streamlit
* Uvicorn

## Installation and Usage
The updated database dump of the LG is available in the following [link](https://libgen.rs/dbdumps/). You may use any database server (SQLite, MySQL, PostgreSQL or MariaDB) to use the code. This is advantage of using ORM because you may migrate to any server without any change in the code. 

All you need is to change the path in the sql_app/database.py file. 

```
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://user:password@localhost:3306/db_name'
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app/db_name.db"
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db_name"
```
After changing the path of database, just use following commands in two different terminal. 

```
uvicorn sql_app.main:app --reload
streamlit run stream.py    
```
You will see the following screen in your default browser. 

![screenshoot from the server](https://github.com/bulend-karadag/LGApi_ORM/Screenshot.png?raw=true)


Now, 3 million books are just one click away.  