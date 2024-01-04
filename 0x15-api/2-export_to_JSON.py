#!/usr/bin/python3
"""Export data to JSON format"""


import csv
import json
import requests
import sys


if __name__ == "__main__":
    """Export data to JSON format"""
    user_id = sys.argv[1]
    if user_id.isdigit() is True:
        user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        todos_url = f"{user_url}/todos"
        tasks = []
        completed_tasks = 0
        total_tasks = 0

        todos_res = requests.get(todos_url)
        todos = todos_res.json()
        total_tasks = len(todos)

        user_res = requests.get(user_url)
        user = user_res.json()

        name = user.get("name")
        username = user.get("username")

        [
            tasks.append(todo["title"]) for todo in todos
            if todo["completed"] is True

        ]
        completed_tasks = len(tasks)

        # Print to stdout
        print(f"Employee {name} is done with tasks"
              f"({completed_tasks}/{total_tasks}):")
        for task in tasks:
            print(f"\t {task}")

        # Write to CSV
        with open(f'{user_id}.csv', 'w', newline='') as csvfile:
            fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS',
                          'TASK_TITLE']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                    quoting=csv.QUOTE_ALL)
            [
                writer.writerow({
                    'USER_ID': str(todo.get('userId')),
                    'USERNAME': username,
                    'TASK_COMPLETED_STATUS': str(todo.get('completed')),
                    'TASK_TITLE': todo.get('title')
                }) for todo in todos
            ]

        # Write to JSON
        with open(f"{user_id}.json", "w") as jsonfile:
            json.dump({
                user_id: [{
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": username
                } for todo in todos]
            }, jsonfile)
