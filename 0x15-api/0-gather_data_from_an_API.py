#!/usr/bin/python3
"""
Python script that using RESTAPI for a given employee ID,returns information
about his/her TODO list progress
"""


if __name__ == '__main__':

    import requests
    from sys import argv

    if len(argv) < 2:
        exit()
    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users'
    refined_url_name = '{}/{}'.format(url, id)
    refined_url_todo = '{}/todos'.format(refined_url_name)
    response = requests.get(refined_url_name)
    response_todos = requests.get(refined_url_todo)
    json_response_name = response.json()
    json_response_todo = response_todos.json()
    employee_name = json_response_name["name"]
    i = 0
    j = 0
    tasks = []
    for obj in json_response_todo:
        if obj["completed"] is True:
            i += 1
            tasks.append(obj["title"])
        j += 1
    print("\t Employee {} is done with tasks({}/{}\n):".
          format(employee_name, i, j))
    for task in tasks:
        print("\t{}".format(task))
