#!/usr/bin/python3
"""This using this REST API, for a given employee ID,
exports their information in csv format"""

import csv
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    emp_id = argv[1]
    name = requests.get(url + "/users/{}".format(emp_id)).json().get("username")
    todos = requests.get(url + "/users/{}/todos".format(emp_id)).json()

    with open("{}.csv".format(emp_id), "w") as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos:
            info = [emp_id, name, todo.get("completed"), todo.get("title")]
            csv_writer.writerow(info)
