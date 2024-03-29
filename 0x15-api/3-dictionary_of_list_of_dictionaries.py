#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employees = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            e.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": e.get("username")
                } for t in requests.get(url + "todos",
                                        params={"userId": e.get("id")}).json()]
            for e in employees}, jsonfile)
