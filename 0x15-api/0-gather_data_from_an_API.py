#!/usr/bin/env python3
''' for a given employee ID, returns information about TODO list progress '''
if __name__ == "__main__":
    from requests import get, post
    from sys import argv
    list_to_do = get('https://jsonplaceholder.typicode.com/todos?userId={}'
                     .format(argv[1])).json()
    users = get('https://jsonplaceholder.typicode.com/users/{}'
                .format(argv[1])).json()
    all_to_do = []
    to_do = []
    for i in list_to_do:
        if (i.get('completed') is True):
            to_do.append(i.get('title'))
        else:
            all_to_do.append(i.get('title'))
    print('Employee {} is done with tasks {}/{}:'
          .format(users.get('name'), len(to_do), len(to_do) + len(all_to_do)))
    for j in to_do:
        print('\t{}'.format(j))
