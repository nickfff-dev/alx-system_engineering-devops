#!/usr/bin/python3
"""Export data to JSON format"""


import json
import requests
from sys import argv


if __name__ == "__main__":
    """Export data to JSON format"""
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get(url + "users/" + user_id).json()
    todo = requests.get(url + "todos?userId=" + user_id).json()
    completed = [task for task in todo if task.get("completed") is True]

    data = {user_id: []}
    for task in completed:
        data[user_id].append({'task': task.get('title'),
                              'completed': task.get('completed'),
                              'username': user.get('name')})
    with open(f'{user_id}.json', 'w') as jsonfile:
        json.dump(data, jsonfile)
