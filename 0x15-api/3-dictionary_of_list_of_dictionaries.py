#!/usr/bin/python3
"""Export data to JSON format"""


import json
import requests


if __name__ == "__main__":
    """Gather all tasks from all users"""
    todos_url = "https://jsonplaceholder.typicode.com/todos/"
    users_url = "https://jsonplaceholder.typicode.com/users/"
    todos_res = requests.get(todos_url)
    todos = todos_res.json()
    all_todos_dict = {}
    users_res = requests.get(users_url)
    users = users_res.json()
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        rows = []
        for todo in todos:
            new_dict = {}
            if todo.get("userId") == user_id:
                new_dict["username"] = username
                new_dict["task"] = todo.get("title")
                new_dict["completed"] = todo.get("completed")
                rows.append(new_dict)
        all_todos_dict[user_id] = rows

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_todos_dict, jsonfile)
