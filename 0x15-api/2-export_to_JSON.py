#!/usr/bin/python3
"""
Python script that exports the information from REST API to json file
"""


if __name__ == '__main__':
    import json
    import requests
    from sys import argv

    if len(argv) < 2:
        exit()
    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users'
    refined_url_name = '{}/{}'.format(url, id)
    file_name = '{}.json'.format(id)
    refined_url_todo = '{}/todos'.format(refined_url_name)
    response = requests.get(refined_url_name)
    response_todos = requests.get(refined_url_todo)
    json_response_name = response.json()
    json_response_todo = response_todos.json()
    user_name = json_response_name["username"]
    list_obj = []
    for obj in json_response_todo:
        dict_obj = {}
        dict_obj["task"] = obj["title"]
        dict_obj["completed"] = obj["completed"]
        dict_obj["username"] = user_name
        list_obj.append(dict_obj)
    file_dict = {}
    file_dict[id] = list_obj
    with open(file_name, "w+", encoding="utf-8") as file:
        json.dump(file_dict, file)
