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

    all_employees = requests.get(url + "users").json()

    diction = {}

    for employee in all_employees:

        emp_id = employee.get('id')
        emp_name = employee.get('username')

        tasks = requests.get(url + "users/" + str(emp_id) + "/todos").json()

        key_list = []

        for todo in tasks:
            temp = {}
            temp['username'] = emp_name
            temp['task'] = todo.get('title')
            temp['completed'] = todo.get('completed')
            key_list.append(temp)

        diction[f'{emp_id}'] = key_list

    with open('todo_all_employees.json', 'w') as f:
        f.write(json.dumps(diction))
