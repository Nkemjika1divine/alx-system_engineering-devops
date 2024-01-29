#!/usr/bin/python3
"""This using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    emp_id = argv[1]
    name = requests.get(url + "/users/{}".format(emp_id)).json().get("name")
    todos = requests.get(url + "/users/{}/todos".format(emp_id)).json()

    job_done = []
    jobs = 0
    job_done_count = 0

    for todo in todos:
        jobs += 1
        if todo.get("completed"):
            job_done.append(todo.get("title"))
            job_done_count += 1
    print("Employee {} is done with tasks({}/{}):".format(
        name,
        job_done_count,
        jobs
        )
    )
    for job in job_done:
        print("\t {}".format(job))
