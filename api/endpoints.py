from api.app import app
from flask import request, send_from_directory
from helpers.sqlConnection import get_table, users, message
from bson import json_util
import os

@app.route("/")
def happiness():
    return {"Welcome to the happiness world": "Let's see how happy your employees are!"}

@app.route("/table/<table>")
def table(table):
    return json_util.dumps(get_table(table))

@app.route("/messages")
def insert_message():
    return json_util.dumps(message(request.args.get('idusers'),request.args.get('message_content')))

@app.route("/user")
def insert_user():
    return json_util.dumps(users(request.args.get('name'),request.args.get('lastname'),request.args.get('department')))

