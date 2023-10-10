#!/usr/bin/python3
"""
put.py
"""

import requests
import json

api_url = "https://jsonplaceholder.typicode.com/todos/10"
todo = {"userId": 1, "title": "wash car", "completed": True}
response = requests.put(api_url, json=todo)
print(response.json())
