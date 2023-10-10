#!/usr/bin/python3
"""
post.py
"""

import requests
import json

api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy Milk", "completed": False}
response = requests.post(api_url, json=todo)
print(response.status_code)
print(response.json())



headers = {"Content-Type": "application/json"}
response_json = requests.post(api_url, data=json.dumps(todo), headers=headers)
print(response_json.status_code)
print(response_json.json())