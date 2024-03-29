#!/usr/bin/python3
"""
Python script that exports the information from REST API to CSV
"""


if __name__ == '__main__':
    import csv
    import requests
    from sys import argv

    if len(argv) < 2:
        exit()
    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users'
    refined_url_name = '{}/{}'.format(url, id)
    file_name = '{}.csv'.format(id)
    refined_url_todo = '{}/todos'.format(refined_url_name)
    response = requests.get(refined_url_name)
    response_todos = requests.get(refined_url_todo)
    json_response_name = response.json()
    json_response_todo = response_todos.json()
    user_name = json_response_name["username"]
    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for obj in json_response_todo:
            row = []
            row.append('{}'.format(obj["userId"]))
            row.append('{}'.format(user_name))
            row.append('{}'.format(obj["completed"]))
            row.append('{}'.format(obj["title"]))
            writer.writerow(row)
