#!/usr/bin/python3
"""
Contain function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""


from collections import defaultdict
import re
import requests


def count_words(subreddit, word_list, count_dict=None, after=''):
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
        if count_dict is None:
            count_dict = defaultdict(int)
        for post in data['data']['children']:
            title = post['data']['title'].lower()
            for word in word_list:
                pattern = r'\b{}\b'.format(word)
                if re.search(pattern, title):
                    count_dict[word] += 1
        if 'next' in data['data']:
            next_page = data['data']['children'][-1]['data']['name']
            return count_words(subreddit, word_list, count_dict, next_page)
        else:
            if len(count_dict) == 0:
                return None
            for key, value in sorted(count_dict.items(),
                                     key=lambda x: (-x[1], x[0])):
                print('{}: {}'.format(key, value))
            return count_dict
    else:
        return None
