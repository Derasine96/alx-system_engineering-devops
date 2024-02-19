#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(emp_id)).json()
    uName = user.get("username")
    todos = requests.get(url + "todos", params={"userId": emp_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        task_list = []
        for t in todos:
            task_list.append({
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": uName
            })

        json.dump({emp_id: task_list}, jsonfile)
