#!/usr/bin/python3
"""
A recursive that queries the Reddit API and return a list of containing all the
titles of all hot articles for a given subreddit
"""


import json
import requests


ready = requests.Session()
ready.headers.update({'User-Agent': 'Script'})
ready.allow_redirects = False


def recurse(subreddit, hot_list=[]):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = ready.get(url).json()
    try:
        for item in response['data']['children']:
            hot_list.append(item['data']['title'])
        if response['data']['after']:
            ready.params = {'after': response['data']['after']}
            return recurse(subreddit, hot_list)
        return hot_list
    except Exception:
        return None
