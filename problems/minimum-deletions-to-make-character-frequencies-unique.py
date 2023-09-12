# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/submissions/?envType=daily-question&envId=2023-09-12
from collections import Counter


class Solution:
    # time: o(n), space: o(n)
    def minDeletions(self, s: str) -> int:
        c_map = Counter(s)
        c_counts = list(c_map.values())

        chars = 0
        count_set = set()
        i = 0
        while i < len(c_counts):
            c = c_counts[i]
            if c in count_set:
                chars += 1
                if c_counts[i] != 1:
                    c_counts[i] -= 1
                else:
                    i += 1
            else:
                i += 1
                count_set.add(c)

        return chars 