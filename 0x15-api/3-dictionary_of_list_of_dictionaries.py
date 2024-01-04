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
        rows = []
        for todo in todos:
            one_todo_dict = {}
            if user['id'] == todo['userId']:
                one_todo_dict['username'] = user['username']
                one_todo_dict['task'] = todo['title']
                one_todo_dict['completed'] = todo['completed']
                rows.append(one_todo_dict)
        all_todos_dict[user['id']] = rows

    with open('todo_all_employees.json', 'w') as jsonfile:
        json_obj = json.dumps(all_todos_dict)
        jsonfile.write(json_obj)
