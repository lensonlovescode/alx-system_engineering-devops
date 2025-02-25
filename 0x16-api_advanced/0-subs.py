#!/usr/bin/python3
"""
Contains a function that queries the Reddit API
and returns the number of subscribers
"""
import requests
import json


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API and
    returns the number of subscribers
    """

    url = "https://reddit.com/r/" + subreddit + "/about.json"
    headers = {"User-Agent": "my-bot/0.1"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return (0)

    data = response.json().get('data')

    if (data is None):
        return (0)
    subscribers = data.get('subscribers')

    return (int(subscribers))
