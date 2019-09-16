#!/usr/bin/python3
''' for a given employee ID, returns information about TODO list progress '''
if __name__ == "__main__":
    import csv
    from requests import get, post
    from sys import argv
    list_to_do = get('https://jsonplaceholder.typicode.com/todos?userId={}'
                     .format(argv[1])).json()
    users = get('https://jsonplaceholder.typicode.com/users/{}'
                .format(argv[1])).json()
    usr_id = int(argv[1])
    with open('{}.csv'.format(argv[1]), 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for j in list_to_do:
            writer.writerow([usr_id, users.get('username'),
                             j.get('completed'), j.get('title')])
