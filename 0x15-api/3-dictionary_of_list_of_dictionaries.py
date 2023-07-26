#!/usr/bin/python3
"""
Python script that exports the information from REST API to json file
"""


if __name__ == '__main__':
    import json
    import requests
    from sys import argv

    url = 'https://jsonplaceholder.typicode.com/users'
    file_name = '{}.json'.format("todo_all_employees")
    response = requests.get(url)
    json_response_name = response.json()
    dict_list = {}
    num_users = 0
    for user in json_response_name:
        num_users += 1
        dict_list[user["id"]] = user["username"]
    json_dict = {}
    for i in range(1, num_users + 1):
        url_id = '{}/{}/todos'.format(url, i)
        response_id = requests.get(url_id)
        json_response_id = response_id.json()
        list_user = []
        for id in json_response_id:
            dict_user = {}
            dict_user["username"] = dict_list[i]
            dict_user["tasks"] = id["title"]
            dict_user["completed"] = id["completed"]
            list_user.append(dict_user)
        json_dict[i] = list_user
    print(json_dict)
    with open(file_name, "w+", encoding="utf-8") as file:
        json.dump(json_dict, file)
