#!/usr/bin/python3
''' for a given employee ID, returns information about TODO list progress '''
if __name__ == "__main__":
    import json
    from requests import get, post
    from sys import argv
    list_to_do = get('https://jsonplaceholder.typicode.com/todos?userId={}'
                     .format(argv[1])).json()
    users = get('https://jsonplaceholder.typicode.com/users/{}'
                .format(argv[1])).json()
    dict_ob2 = {}
    val = []
    for j in list_to_do:
        dict1 = {}
        dict1.update({'task': j.get('title')})
        dict1.update({'completed': j.get('completed')})
        dict1.update({'username': users.get('username')})
        val.append(dict1)
    dict_ob2.update({argv[1]: val})
    with open('{}.json'.format(argv[1]), 'w', newline='') as json_file:
            json_file.write(json.dumps(dict_ob2) + '\n')
