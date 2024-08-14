#!/usr/bin/python3
"""
This script queries the Reddit API for some requests
"""

import requests


def number_of_subscribers(subreddit) -> int:
    """
    This function queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    args:
        subreddit: string
    return: 0 If an invalid subreddit is given
    """

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        else:
            return 0
    except requests.RequestException:
        return 0
