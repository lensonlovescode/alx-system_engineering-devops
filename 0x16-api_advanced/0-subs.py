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

    url = "https://reddit.com/r/" + subreddit + ".json?limit=1"
    headers = {"User-Agent": "my-bot/0.1"}

    response = requests.get(url, headers=headers).json()
    data = response.get('data')
    children = data.get('children')

    return(int(children[0].get('data').get('subreddit_subscribers')))
