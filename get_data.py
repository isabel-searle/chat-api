
import requests
import pandas as pd
from datetime import datetime


def get_all_messages():
    url = "http://127.0.0.1:5000/table/messages"
    text = requests.get(url)
    to_analize = [i['message_content'] for i in text.json()] 
    return to_analize


def get_messages_by_dept(dept):
    try:
        pass
    except NameError:
        dept=str(dept)
        pass
    messages = requests.get("http://127.0.0.1:5000/table/messages")
    users = requests.get("http://127.0.0.1:5000/table/users")
    df_messages=pd.DataFrame(messages.json())
    df_users=pd.DataFrame(users.json())
    df_merged=df_users.merge(df_messages)
    df_merged['date_time'] = [i['$date']/1000 for i in df_merged['date_time']]
    df_merged['date_time'] = df_merged['date_time'].map(lambda x: datetime.fromtimestamp(x).strftime("%d/%m/%Y, %H:%M:%S")) 
    return list(df_merged[df_merged['department']==dept]['message_content'])
    


def get_messages_by_date(date):
    if type(date) == str:
        if "-" in date:
            date=date.replace("-","/")
        else:
            pass
        messages = requests.get("http://127.0.0.1:5000/table/messages")
        users = requests.get("http://127.0.0.1:5000/table/users")
        df_messages=pd.DataFrame(messages.json())
        df_users=pd.DataFrame(users.json())
        df_merged=df_users.merge(df_messages)
        df_merged['date_time'] = [i['$date']/1000 for i in df_merged['date_time']]
        df_merged['date_time'] = df_merged['date_time'].map(lambda x: datetime.fromtimestamp(x).strftime("%d/%m/%Y")) 
        return list(df_merged[df_merged['date_time']==date]['message_content'])
    else:
        raise TypeError("Enter a string %d/%m/%Y")      


def get_complet_table():
    messages = requests.get("http://127.0.0.1:5000/table/messages")
    users = requests.get("http://127.0.0.1:5000/table/users")
    df_messages=pd.DataFrame(messages.json())
    df_users=pd.DataFrame(users.json())
    df_merged=df_users.merge(df_messages)
    df_merged['date_time'] = [i['$date']/1000 for i in df_merged['date_time']]
    df_merged['date_time'] = df_merged['date_time'].map(lambda x: datetime.fromtimestamp(x).strftime("%d/%m/%Y, %H:%M:%S"))
    return df_merged