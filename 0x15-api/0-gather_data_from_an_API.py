#!/usr/bin/python3
"""Gather data from an API"""


import requests
from sys import argv


def get_tasks_done(employeeId):
    """Get tasks done"""
    todos_res = requests.get("https://jsonplaceholder.typicode.com/todos/")
    todos = todos_res.json()
    completed_tasks = 0
    total_tasks = 0
    tasks = []
    users_res = requests.get("https://jsonplaceholder.typicode.com/users/")
    users = users_res.json()
    for user in users:
        if user.get("id") == int(employeeId):
            username = user.get("name")
    for todo in todos:
        if todo.get("userId") == int(employeeId):
            total_tasks += 1
            if todo.get("completed") is True:
                completed_tasks += 1
                tasks.append(todo.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(username,
                                                          completed_tasks,
                                                          total_tasks))
    for task in tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    get_tasks_done(argv[1])
