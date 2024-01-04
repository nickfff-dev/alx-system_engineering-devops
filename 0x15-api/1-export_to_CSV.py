#!/usr/bin/python3
"""Gather data from an API and export to CSV"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    """Gather data from an API and export to CSV"""
    todos_res = requests.get("https://jsonplaceholder.typicode.com/todos/")
    todos = todos_res.json()
    users_res = requests.get("https://jsonplaceholder.typicode.com/users/")
    users = users_res.json()
    for user in users:
        if user['id'] == int(argv[1]):
            user_id = user['id']
            username = user['username']
    with open(f'{user_id}.csv', 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS',
                      'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for task in todos:
            row = {}
            if task['userId'] == int(argv[1]):
                row['USER_ID'] = user_id
                row['USERNAME'] = username
                row['TASK_COMPLETED_STATUS'] = task['completed']
                row['TASK_TITLE'] = task['title']
                writer.writerow(row)
