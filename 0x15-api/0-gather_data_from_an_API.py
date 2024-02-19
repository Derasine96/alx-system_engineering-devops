#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    user_response = requests.get(url)
    data = user_response.json()

    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    t_response = requests.get(url)
    t_response = requests.get(url)
    t_data = t_response.json()

    total = len(t_data)
    done_task = len([todo for todo in t_data if todo['completed']])

    print("Employee {} is done with tasks({}/{}):".format(data.get('name'),
                                                          done_task, total))
    for todo in t_data:
        if todo['completed']:
            print('\t ' + todo['title'])
