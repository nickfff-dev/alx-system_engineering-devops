#!/usr/bin/python3
"""Gather data from an API"""


import requests
from sys import argv


if __name__ == "__main__":
    """Gather data from an API"""
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get(url + "users/" + user_id).json()
    todo = requests.get(url + "todos", params={"userId": user_id}).json()
    completed = [task.get("title") for task in todo if
                 task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todo)))
    [print("\t {}".format(task)) for task in completed]
