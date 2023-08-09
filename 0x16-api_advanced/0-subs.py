#!/usr/bin/python3
"""
Python script that exports the information from REST API to json file
"""


import json
import requests
from sys import argv


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url)
    json_response_name = response.json()
    try:
        return json_response_name["data"]["subscribers"]
    except Exception:
        return 0
