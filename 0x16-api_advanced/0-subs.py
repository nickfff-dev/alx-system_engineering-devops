#!/usr/bin/python3
"""function that queries the Reddit API and returns the number
of subscribers (not active users, total subscribers) for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/70.0.3538.77 Safari/537.36'}
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        data = r.json()
        subs = data.get('data').get('subscribers')
        if subs is None:
            return 0
    else:
        return 0
