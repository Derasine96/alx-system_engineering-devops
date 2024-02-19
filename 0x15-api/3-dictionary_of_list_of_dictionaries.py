#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import requests
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employees_response = requests.get(url + "users")
    employees = employees_response.json()

    tasks_dict = {}
    for emp in employees:
        todos_response = requests.get(url + "todos",
                                      params={"userId": emp.get("id")})
        todos = todos_response.json()
        tasks_list = [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "uName": emp.get("username")
            }
            for t in todos
        ]
        tasks_dict[emp.get("id")] = tasks_list

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(tasks_dict, jsonfile)
