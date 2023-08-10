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
    string = ""
    try:
        data = response['data']['children'][i]
        string = data['data']['title']
        hot_list.append(string)
    except IndexError:
        return hot_list
    return recurse(subreddit, hot_list, i+1)
