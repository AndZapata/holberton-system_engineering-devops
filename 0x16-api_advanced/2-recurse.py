#!/usr/bin/python3
''' Comment: start point'''
from requests import get
after = ''


def recurse(subreddit, hot_list=[]):
    ''' recursive function to obtain a list of top titles in all pages '''
    global after
    header = {'User-Agent': 'My User Agent 1.0'}
    try:
        url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
        if after:
            url = url + '?after={}'.format(after)
        getting = get(url, headers=header, allow_redirects=False).json()
        for children in getting['data']['children']:
            hot_list.append(children.get('data').get('title'))
        after = get(url, headers=header,
                    allow_redirects=False).json().get('data').get('after')
        if after:
            return recurse(subreddit, hot_list)
        return hot_list
    except:
        return None
