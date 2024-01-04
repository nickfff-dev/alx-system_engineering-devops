#!/usr/bin/python3
"""Export data to JSON format"""


import json
import requests
from sys import argv


if __name__ == "__main__":
    """Export data to JSON format"""
    todos_res = requests.get("https://jsonplaceholder.typicode.com/todos/")
    todos = todos_res.json()
    users_res = requests.get("https://jsonplaceholder.typicode.com/users/")
    users = users_res.json()

    for user in users:
        if user.get("id") == int(argv[1]):
            user_id = user.get("id")
            username = user.get("username")
    rows = []

    for todo in todos:
        new_dict = {}
        if todo.get("userId") == int(argv[1]):
            new_dict["task"] = todo.get("title")
            new_dict["completed"] = todo.get("completed")
            new_dict["username"] = username
            rows.append(new_dict)

    json_dict = {}
    json_dict[user_id] = rows
    json_obj = json.dumps(json_dict)

    with open(f"{user_id}.json", "w") as jsonfile:
        jsonfile.write(json_obj)
