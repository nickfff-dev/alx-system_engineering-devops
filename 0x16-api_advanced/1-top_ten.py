#!/usr/bin/python3
"""Contain function that queries the Reddit API"""


import requests


def top_ten(subreddit):
    """Print the titles of the top 10 hot posts for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/70.0.3538.77 Safari/537.36'}
    if subreddit is None or type(subreddit) is not str:
        print("None")
        return
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        data = r.json()
        if 'error' in data:
            print("None")
            return
        if len(data['data']['children']) == 0:
            print("None")
            return
        for post in data['data']['children']:
            print(post['data']['title'])
        return
    else:
        print("None")
        return
