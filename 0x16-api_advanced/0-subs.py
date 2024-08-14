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
    # Defne url to query
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    # Set custom User-Agent to avoid Too Many Requests error
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check for successful request
        if response.status_code == 200:
            # Parse JSON response
            data = response.json()
            # Return subscribers
            return data.get("data", {}).get("subscribers", 0)
        else:
            # Return 0 if invalid subreddit
            return 0
    except requests.RequestException:
        # Handle request exception
        return 0
