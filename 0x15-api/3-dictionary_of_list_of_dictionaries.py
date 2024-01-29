#!/usr/bin/python3
"""This file is for testing the codes"""
import json
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    with open("todo_all_employees.json", "w") as f:
        obj = {}
        emp_id = 0  # id of the employees
        while True:
            emp_id += 1
            emp = requests.get(url + "/users/{}".format(
                emp_id
                )).json().get("username")
            if not emp:
                break
            todos = requests.get(url + "/users/{}/todos".format(emp_id)).json()
            value_list = []
            for todo in todos:
                values = {}
                values["task"] = todo.get("title")
                values["completed"] = todo.get("completed")
                values["username"] = emp
                value_list.append(values)
            obj[emp_id] = value_list
        json.dump(obj, f)
