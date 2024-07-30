#!/usr/bin/python3
""" This module fetches information from a URL """
from requests import get
from sys import argv
import urllib.request


if __name__ == "__main__":
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    res = get(url)
    name = res.json().get('name')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    res = get(url)
    tasks = res.json()
    done = 0
    completed_tasks = []
    for task in tasks:
        if task.get('completed'):
            completed_tasks.append(task)
            done += 1

    print(f"Employee {name} is done with tasks({done}/{len(tasks)}):")
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
