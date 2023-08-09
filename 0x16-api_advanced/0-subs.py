#!/usr/bin/python3
"""
Python script that exports the information from REST API to json file
"""


if __name__ == '__main__':
    import json
    import requests
    from sys import argv

    def number_of_subscribers(subreddit):
        url = 'https://www.reddit.com/r/{}/about.json'.format(argv[2])
        response = requests.get(url)
        json_response_name = response.json()
        print(json_response_name)
