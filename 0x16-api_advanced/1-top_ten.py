#!/usr/bin/python3
"""
Python script that exports the information from REST API to json file
"""


import json
import requests
from sys import argv


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url).json()
    data = response['data']
    if data['children']:
        for title in data['children'][:10]:
            print(title)['data']['title']
        else:
            print(None)
