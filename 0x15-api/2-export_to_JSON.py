#!/usr/bin/python3
"""This using this REST API, for a given employee ID,
exports their information in csv format"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    emp_id = argv[1]
    emp = requests.get(url + "/users/{}".format(emp_id)).json().get("username")
    todos = requests.get(url + "/users/{}/todos".format(emp_id)).json()

    with open("{}.json".format(emp_id), "w") as f:
        obj = {}
        value_list = []
        for todo in todos:
            values = {}
            values["task"] = "{}".format(todo.get("title"))
            values["completed"] = "{}".format(todo.get("completed"))
            values["username"] = emp
            value_list.append(values)
        obj[emp_id] = value_list
        json.dump(obj, f)
