from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
load_dotenv()

user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASS")
mysql_url = f'mysql+mysqldb://{user}:{password}@localhost'
engine = create_engine(mysql_url)
conn = engine.connect()
conn.execute('USE chat_api;')

def get_table(table):
    query = f"SELECT * FROM {table};"
    res = conn.execute(query)
    return list(res)

def users(name, lastname, department):
    query = f"INSERT INTO users (name, lastname, department) VALUES ('{name}', '{lastname}', '{department}')"
    res = conn.execute(query)
    return {"insertion": "ok"}

def message(idusers, message_content):
    query = f"INSERT INTO messages (idusers, message_content, date_time) VALUES ({idusers}, '{message_content}', NOW())"
    res = conn.execute(query) 
    return {"insertion": "done"}


