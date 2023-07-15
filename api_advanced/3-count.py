#!/usr/bin/python3
""" 3-count.py """
import json
import requests


def count_words(subreddit, word_list, after="", count=None):
    """ prints a sorted count of given keywords """
    if count is None:
        count = [0] * len(word_list)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        for topic in data['data']['children']:
            for word in topic['data']['title'].split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        count[i] += 1

        after = data['data']['after']
        if after is None:
            save = set()
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        save.add(j)
                        count[i] += count[j]

            word_count_pairs = sorted(zip(word_list, count), key=lambda x: (-x[1], x[0]))

            for word, count in word_count_pairs:
                if count > 0 and i not in save:
                    print(f"{word.lower()}: {count}")
        else:
            count_words(subreddit, word_list, after, count)


