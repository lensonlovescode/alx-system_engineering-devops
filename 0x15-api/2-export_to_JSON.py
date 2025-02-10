#!/usr/bin/python3
"""
Using what was done in task #0, this py script extends
to export the data gathered in the CSV format.
"""
import csv
import json
import requests
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"

    name = requests.get(url + "users/" + sys.argv[1]).json().get('username')
    tasks = requests.get(url + "users/" + sys.argv[1] + "/todos").json()

    key_list = []

    with open(f'{sys.argv[1]}.json', 'w') as f:

        for todo in tasks:
            temp = {}
            temp['task'] = todo.get('title')
            temp['completed'] = todo.get('completed')
            temp['username'] = name
            key_list.append(temp)

        diction = {}
        diction[f'{sys.argv[1]}'] = key_list

        f.write(json.dumps(diction))
