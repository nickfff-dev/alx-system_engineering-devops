#!/usr/bin/python3
"""Export data to JSON format"""


import json
import requests


if __name__ == "__main__":
    """Gather all tasks from all users"""
    todos_res = requests.get("https://jsonplaceholder.typicode.com/todos/")
    todos = todos_res.json()
    all_todos_dict = {}
    users_res = requests.get("https://jsonplaceholder.typicode.com/users/")
    users = users_res.json()
    for user in users:
        user_todos_list = []
        for task in todos:
            if task.get("userId") == user.get("id"):
                user_todos_list.append({"username": user.get("username"),
                                        "task": task.get("title"),
                                        "completed": task.get("completed")})
        all_todos_dict[user.get("id")] = user_todos_list
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_todos_dict, jsonfile)
