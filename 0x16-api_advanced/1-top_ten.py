#!/usr/bin/python3
"""
Contains a function that queries the Reddit API and
prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests
import json


def top_ten(subreddit):
    """
    A function that queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit.
    """
    url  = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=9"
    headers = {"User-Agent": "my-bot/0.1"}
    
    request = requests.get(url, headers=headers, allow_redirects=False)

    if request.status_code != 200:
        print('None')
        return

    posts = request.json().get('data').get('children')

    for post in posts:
        data = post.get('data')
        title = data.get('title')
        print(title)
