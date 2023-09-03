# Interview questions with company - GreenArc Capital Pte Ltd -

# 1. Write a function/program to create and hold a session.

# Solution - What are sessions? - Session Objects – Python requests -

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


# 2. Write a function/program to implement login functionality in Python.


# 3. Write a function/program to search for Anagrams from a list items.

# Solution - https://ytube.io/3jDy

# from collections import defaultdict
# # from collections.abc import dict_values
# from typing import Any
#
#
# class Solution:
#     def groupAnagrams(self, strs: list[str]):
#         # res = {} # mapping char-count to list of anagrams
#         res = defaultdict(list)  # mapping char-count to list of anagrams
#
#         for s in strs:
#             char_count = [0] * 26  # a..z
#
#             for c in s:
#                 char_count[ord(c) - ord("a")] += 1
#
#             res[tuple(char_count)].append(s)
#
#         return res.values()
