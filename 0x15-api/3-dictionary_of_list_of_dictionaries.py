#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employees = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        tasks_dict = {}
        for emp in employees:
            emp_id = emp.get("id")
            todos_response = requests.get(url + "todos",
                                          params={"userId": emp_id})
            todos = todos_response.json()
            tasks_list = []
            for t in todos:
                todo_dict = {
                    "task": t.get("title"),
                    "completed": t.get("completed"),
                    "uName": emp.get("username")
                }
                tasks_list.append(todo_dict)
            tasks_dict[emp_id] = tasks_list
        json.dump(tasks_dict, jsonfile)
