#!/usr/bin/python3
""" Contain function that queries the Reddit API and returns a list
"""


import requests


def recurse(subreddit, hot_list=[], after=''):
    """Recursively fetch the titles of
    all hot posts for a given subreddit."""
    base_url = 'https://www.reddit.com/r/{}/hot.json?limit=100&after={}'
    url = base_url.format(subreddit, after)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/70.0.3538.77 Safari/537.36'}
    if subreddit is None or type(subreddit) is not str:
        return None
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        data = r.json()
        if 'error' in data:
            return None
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        if 'next' in data['data']:
            return recurse(subreddit, hot_list,
                           data['data']['children'][-1]['data']['name'])
        else:
            return hot_list
    else:
        return None
