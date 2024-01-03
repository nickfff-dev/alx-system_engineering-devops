#!/usr/bin/python3
"""Gather data from an API and export to CSV"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    """Gather data from an API and export to CSV"""
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get(url + "users/" + user_id).json()
    todo = requests.get(url + "todos?userId=" + user_id).json()
    completed = [task for task in todo if task.get("completed") is True]
    with open(f'{user_id}.csv', 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS',
                      'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in todo:
            writer.writerow({
                'USER_ID': user_id,
                'USERNAME': user.get('username'),
                'TASK_COMPLETED_STATUS': str(task.get('completed')),
                'TASK_TITLE': task.get('title')
            })
