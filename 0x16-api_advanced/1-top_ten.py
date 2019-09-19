#!/usr/bin/python3
''' Comment: start point'''
from requests import get


def top_ten(subreddit):
    ''' Prints the ten hot posts '''
    header = {'User-Agent': 'My User Agent 1.0'}
    try:
        url = get('https://www.reddit.com/r/{}.json?limit=10&sort=hot'
                  .format(subreddit),
                  headers=header, allow_redirects=False).json()
        for childrend in url['data']['children']:
            print(childrend['data']['title'])
    except:
        print(None)
