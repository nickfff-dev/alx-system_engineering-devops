#!/usr/bin/python3
"""Export data to JSON format"""


import json
import requests


def gather_tasks():
    """Gather all tasks from all users"""
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()
    data = {}
    for user in users:
        user_id = user['id']
        user_todos = [task for task in todos if task['userId'] == user_id]
        data[user_id] = [{'username': user['name'],
                          'task': task['title'],
                          'completed': task['completed']}
                         for task in user_todos]
    return data


if __name__ == "__main__":
    data = gather_tasks()
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(data, jsonfile)
