#!/usr/bin/python3
''' for a given employee ID, returns information about TODO list progress '''
if __name__ == "__main__":
    import json
    from requests import get

    users = get('https://jsonplaceholder.typicode.com/users').json()
    l_todo = get('https://jsonplaceholder.typicode.com/todos').json()
    dict2 = {i.get('id'): [] for i in users}
    dict_u = {i.get('id'): i.get("username") for i in users}

    for j in l_todo:
        dict1 = {}
        usr_id = j.get('userId')
        dict1.update({'task': j.get('title')})
        dict1.update({'completed': j.get('completed')})
        dict1.update({"username": dict_u.get(usr_id)})
        dict2.get(usr_id).append(dict1)

    with open('todo_all_employees.json', 'w') as json_file:
            json.dump(dict2, json_file)
