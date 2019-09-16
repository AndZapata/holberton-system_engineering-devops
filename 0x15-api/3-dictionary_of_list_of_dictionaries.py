#!/usr/bin/python3
''' for a given employee ID, returns information about TODO list progress '''
if __name__ == "__main__":
    import json
    from requests import get, post
    from sys import argv
    users = get('https://jsonplaceholder.typicode.com/users').json()
    list1 = []
    dict_ob2 = {}
    val = []
    for i in users:
        list1.append(i.get('id'))
        for usr_id in list1:
            l_todo = get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(usr_id)).json()
            for j in l_todo:
                dict1 = {}
                dict1.update({'task': j.get('title')})
                dict1.update({'completed': j.get('completed')})
                dict1.update({'username': i.get('username')})
                val.append(dict1)
    dict_ob2.update({usr_id: val})
    with open('todo_all_employees.json'.format(usr_id),
              'w', newline='') as json_file:
        json_file.write(json.dumps(dict_ob2) + '\n')
