#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]
    user_url = (
                f'https://jsonplaceholder.typicode.com/users/{emp_id}'
                )
    todo_url = (
                f'https://jsonplaceholder.typicode.com/users/{emp_id}/todos'
                )
    user_response = requests.get(user_url)
    user_response.raise_for_status()
    user_dat = user_response.json()

    t_response = requests.get(todo_url)
    t_response.raise_for_status()
    t_data = t_response.json()

    total = len(t_data)
    done = len([todo for todo in t_data if todo['completed']])

    print("Employee {} is done with tasks({}/{}):".format(user_dat.get('name'),
                                                          done, total))
    for todo in t_data:
        if todo['completed']:
            print('\t ' + todo['title'])
