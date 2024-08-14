#!/usr/bin/python3
""" This module fetches information from a URL and exports it in a JSON file"""
from json import dump
from requests import get


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'
    res = get(url)
    users = res.json()

    dictionary = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        response = get(url)
        tasks = response.json()
        dictionary[user_id] = []
        for task in tasks:
            dictionary[user_id].append({
                                        "task": task.get('title'),
                                        "completed": task.get('completed'),
                                        "username": username
                                        })
    with open('todo_all_employees.json', 'w') as file:
        dump(dictionary, file)