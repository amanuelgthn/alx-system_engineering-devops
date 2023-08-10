#!/usr/bin/python3
"""
A recursive that queries the Reddit API and return a list of containing all the
titles of all hot articles for a given subreddit
"""


import json
import requests


def recurse(subreddit, hot_list=[], i=0):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url=url,
                            headers=headers,
                            allow_redirects=False).json()
    try:
        data = response['data']['children'][i]
        hot_list.append(data['data']['title'])
    except Exception:
        print(None)
        return
    return recurse(subreddit, hot_list, i)
