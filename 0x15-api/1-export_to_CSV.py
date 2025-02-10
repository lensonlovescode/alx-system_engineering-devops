#!/usr/bin/python3
"""
Using what was done in task #0, this py script extends
to export the data gathered in the CSV format.
"""
import csv
import requests
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"

    name = requests.get(url + "users/" + sys.argv[1]).json().get('name')
    tasks = requests.get(url + "users/" + sys.argv[1] + "/todos").json()

    biglist = []

    with open(f'{sys.argv[1]}.csv', 'w') as f:

        for todo in tasks:
            userid = todo.get('userId')
            i_d = todo.get('id')
            title = todo.get('title')
            done = todo.get('completed')
            f.write(f'"{userid}","{name}","{done}","{title}"\n')
