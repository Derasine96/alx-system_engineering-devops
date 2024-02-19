#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import json
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(emp_id)).json()
    uName = user.get("username")
    todos = requests.get(url + "todos", params={"userId": emp_id}).json()

    with open("{}.json".format(emp_id), "w") as jsonfile:
        tasks_dict = {emp_id: []}
        for t in todos:
            task_dict = {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": uName
            }
            tasks_dict[emp_id].append(task_dict)
        json.dump(tasks_dict, jsonfile)
