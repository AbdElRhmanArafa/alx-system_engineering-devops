#!/usr/bin/python3

"""
This module fetches the TODO list progress for a given employee ID
from a REST API and displays it.
It uses the 'requests' library to make HTTP requests.
"""

import requests
import sys


def fetch_todo_list_progress(employee_id):
    """
    Fetches and prints the TODO list progress for the specified employee ID.

    Args:
    employee_id (int): The ID of the employee whose TODO
    list progress is to be fetched.

    Returns:
    None
    """
    # Define the base URL for fetching user data and todos
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Failed to retrieve data for employee ID {employee_id}")
        return

    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch todos data
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Failed to retrieve TODO data for employee ID {employee_id}")
        return

    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo.get('completed'))

    # Output the results
    print(f"Employee {employee_name} is done with tasks /
          ({completed_tasks} / {total_tasks}): ")
    for todo in todos_data:
        if todo.get('completed'):
            print(f"\t {todo.get('title')}")


def main():
    employee_id = sys.argv[1]
    fetch_todo_list_progress(employee_id)


if __name__ == "__main__":
    main()
