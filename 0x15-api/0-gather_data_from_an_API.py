#!/usr/bin/python3
"""Gather data from an API"""


import requests
import sys


if __name__ == "__main__":
    """Get tasks done"""
    user_id = sys.argv[1]
    if user_id.isdigit() is True:
        todos_res = requests.get("https://jsonplaceholder.typicode.com/todos/")
        todos = todos_res.json()
        completed_tasks = 0
        total_tasks = 0
        tasks = []
        users_res = requests.get("https://jsonplaceholder.typicode.com/users/")
        users = users_res.json()
        for user in users:
            if user["id"] == int(sys.argv[1]):
                username = user["name"]
        for todo in todos:
            if todo["userId"] == int(sys.argv[1]):
                total_tasks += 1
                if todo["completed"] is True:
                    completed_tasks += 1
                    tasks.append(todo["title"])
        # Print to stdout
        print(f"Employee {username} is done with tasks"
              f"({completed_tasks}/{total_tasks}):")
        for task in tasks:
            print(f"\t {task}")
