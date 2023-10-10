#!/usr/bin/python3
"""
delete.py
"""

import requests
import json

api = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.delete(api)
print(response.json())