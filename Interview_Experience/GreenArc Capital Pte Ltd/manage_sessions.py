# Interview questions with company - GreenArc Capital Pte Ltd -

# 1. Write a function/program to create and hold a session.

# Solution - Reference -
# 1. https://bityl.co/Ks2p
# 2. https://www.youtube.com/watch?v=8qsNauBEVNM&t=26s&ab_channel=DanLeeman

# What are sessions? - Session Objects – Python requests -

# Session object allows one to persist certain parameters across requests. It also persists cookies across all
# requests made from the Session instance and will use urllib3’s connection pooling. So, if several requests are
# being made to the same host, the underlying TCP connection will be reused, which can result in a significant
# performance increase. A session object all the methods as of requests.

# Sample program to demonstrate the same -

import requests

a = requests.Session()
userName = {"userName": "Swapnadeep"}
location = {"location": "NewTown"}

setCookieURL = "https://httpbin.org/cookies/set"
getCookieURL = "https://httpbin.org/cookies"

a.get(setCookieURL, params=userName)
a.get(setCookieURL, params=location)

r = a.get(getCookieURL)
print(r.text)


# 2. Write a function/program to implement login functionality in Python -

# Solution reference -
# 1. https://bityl.co/Ks2l
# 2. https://ytube.io/3jMp

def login(users):
    while True:
        username = input("Please enter your username")
        password = input("Please enter your password")

        for u in users:
            if username == u[0]:
                if password == u[1]:
                    return username
        print("Username or Password is incorrect, please try again later!")


users = [['patrician', 'abc123'], ['dizzy', 'def456'], ['rygar', 'ghi789']]

username = login(users)

print(username, "has logged-in")

# 3. Write a function/program to search for Anagrams from a list items.

# Solution - https://ytube.io/3jDy

from collections import defaultdict


# from collections.abc import dict_values


class Solution:
    def groupAnagrams(self, strs: list[str]):
        # res = {} # mapping char-count to list of anagrams
        res = defaultdict(list)  # mapping char-count to list of anagrams

        for s in strs:
            char_count = [0] * 26  # a..z

            for c in s:
                char_count[ord(c) - ord("a")] += 1

            res[tuple(char_count)].append(s)

        return res.values()
