#!/usr/bin/python3
"""Gather data from an API"""


import requests
from sys import argv


def get_tasks_done(employeeId):
    """Get tasks done"""
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employeeId)).json()
    todo = requests.get(url + "todos", params={"userId": employeeId}).json()
    completed = [task.get("title") for task in todo if
                 task.get("completed") is True]
    print("Employee {:s} is done with tasks({:d}/{:d}):".format(
        user.get("name"), len(completed), len(todo)))
    [print("\t {}".format(task)) for task in completed]


if __name__ == "__main__":
    get_tasks_done(argv[1])
