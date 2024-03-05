#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""
import requests


def count_words(subreddit, word_list, after='', word_dict={}):
    """Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    if not word_dict:
        for word in word_list:
            if word.lower() not in word_dict:
                word_dict[word.lower()] = 0
    if after is None:
        worddict = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word in worddict:
            if word[1]:
                print('{}: {}'.format(word[0], word[1]))
        return None
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/Derasine96)"
    }
    params = {
        "after": after,
        "limit": 100
    }
    response = requests.get(url, headers=header, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        hot = response.json()['data']['children']
        aft = response.json()['data']['after']
        for post in hot:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]

            for word in word_dict.keys():
                word_dict[word] += lower.count(word)

    except Exception:
        return None

    count_words(subreddit, word_list, aft, word_dict)
