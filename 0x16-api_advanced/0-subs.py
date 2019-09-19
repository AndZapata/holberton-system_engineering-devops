#!/usr/bin/python3
''' Comment: start point '''
from requests import get


def number_of_subscribers(subreddit):
    ''' Function to return the subs in a subreddit '''
    header = {'User-Agent': 'My User Agent 1.0'}
    try:
        url = get('https://www.reddit.com/r/{}/about.json'.format(subreddit),
                  headers=header, allow_redirects=False).json()
        return url.get('data').get('subscribers')
    except:
        return 0
