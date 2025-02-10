#!/usr/bin/python3
"""
Contains a py script that using thie given REST API
for a given employee ID, returns information about his/her TODO list progress
"""
import requests
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"

    name = requests.get(url + "users/" + sys.argv[1]).json().get('name')
    tasks = requests.get(url + "users/" + sys.argv[1] + "/todos").json()

    checklist = []
    done = 0
    total = 0

    for todo in tasks:
        if todo.get('completed') is True:
            done += 1
            checklist.append(todo.get('title'))
        total += 1

    print(f"Employee {name} is done with tasks({done}/{total}):\n\t ", end="")

    print('\n\t '.join(checklist))
