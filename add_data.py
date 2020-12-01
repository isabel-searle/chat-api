import pandas as pd
from faker import Faker
import requests
import random

def add_fake_messages(num_of_msg):
    try:
        messages = [faker.text(max_nb_chars=40) for i in range(num_of_msg)]
    except TypeError:
        raise TypeError("Enter an integer")
        users = requests.get("http://127.0.0.1:5000/table/users")
        for i in messages:
            iduser=random.randint(0,len(users.json()))
            url = f"http://127.0.0.1:5000/messages?idusers={iduser}&message_content={i}"
        return requests.get(url)


def add_messages(message):
    users = requests.get("http://127.0.0.1:5000/table/users")
    iduser=random.randint(0,len(users.json()))
    url = f"http://127.0.0.1:5000/messages?idusers={iduser}&message_content={message}"
    return requests.get(url)


def add_messages_by_dept(message, dept):
    users = requests.get("http://127.0.0.1:5000/table/users")
    df_users=pd.DataFrame(users.json())
    us=df_users[df_users['department']==dept]['idusers'].tolist()
    iduser=random.choice(us)
    url = f"http://127.0.0.1:5000/messages?idusers={iduser}&message_content={message}"
    return requests.get(url)

