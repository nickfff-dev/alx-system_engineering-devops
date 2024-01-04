#!/usr/bin/python3
"""Gather data from an API and export to CSV"""

import csv
import requests
import sys


if __name__ == "__main__":
    """Gather data from an API and export to CSV"""
    user_id = sys.argv[1]
    todos_url = "https://jsonplaceholder.typicode.com/todos/"
    users_url = "https://jsonplaceholder.typicode.com/users/"
    if user_id.isdigit() is True:
        todos_res = requests.get(todos_url)
        todos = todos_res.json()
        completed_tasks = 0
        total_tasks = 0
        tasks = []
        users_res = requests.get(users_url)
        users = users_res.json()

        for user in users:
            if user["id"] == int(sys.argv[1]):
                username = user["username"]
                name = user["name"]
                user_id = user["id"]

        for todo in todos:
            if todo["userId"] == int(sys.argv[1]):
                total_tasks += 1
                if todo["completed"] is True:
                    completed_tasks += 1
                    tasks.append(todo["title"])

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
            for i in todos:
                row = {}
                if i['userId'] == int(sys.argv[1]):
                    row['USER_ID'] = i.get('userId')
                    row['USERNAME'] = username
                    row['TASK_COMPLETED_STATUS'] = i.get('completed')
                    row['TASK_TITLE'] = i.get('title')
                    writer.writerow(row)
