#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": '0x16-api_advanced:project:v1.0.0(by /u/Derasine96)'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200 and not response.is_redirect:
        results = response.json().get("data")
        return results.get("subscribers")
    return 0
