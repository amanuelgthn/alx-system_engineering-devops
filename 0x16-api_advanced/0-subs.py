#!/usr/bin/python3
"""
Script that queries the REDDIT API and number of subscribers of a subreddit
"""


import json
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """
    function that queries the reddit API and returns the number of subscribers
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url)
    json_response_name = response.json()
    try:
        return json_response_name['data']["subscribers"]
    except Exception:
        return 0
