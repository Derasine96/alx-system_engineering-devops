#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyRedditBot/1.0"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print("None")
    else:
        print(f"None")
