# Interview questions with GreenArc Capital Pte Ltd -

# 1. Write a function/program to create and hold a session.
# 2. Write a function/program to implement login functionality in Python.
# 3. Write a function/program to search for Anagrams from a list items.

# solution approach followed - https://ytube.io/3jDy
from collections import defaultdict
# from collections.abc import dict_values
from typing import Any


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
