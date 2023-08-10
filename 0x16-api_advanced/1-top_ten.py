#!/usr/bin/python3
"""
Python script that exports the information from REST API to json file
"""


import json
import requests
from sys import argv


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url=url,
                            headers=headers,
                            allow_redirects=False).json()
    for i in range(9):
        try:
            data = response['data']['children'][i]
            print(data['data']['title'])
        except Exception:
            print(None)
