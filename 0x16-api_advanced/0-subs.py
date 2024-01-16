#!/usr/bin/python3
"""
Contain function that queries the Reddit API and returns sub
"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers"""
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/70.0.3538.77 Safari/537.36'}
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        data = r.json()
        subname = data.get('data', {}).get('display_name', None)
        if subname is None or subname.lower() != subreddit.lower():
            return 0
        return data.get('data', {}).get('subscribers', 0)
