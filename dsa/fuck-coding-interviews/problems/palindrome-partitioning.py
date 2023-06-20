# https://leetcode.com/problems/palindrome-partitioning/description/


from . import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        def backtrack(index=0):
            if index == len(s):
                res.append(path.copy())
                return
            # base-condition:
            for i in range(index, len(s)):
                st = s[index:i+1]
                # check if st is palindrome:
                if len(st) == 1 or st == st[::-1]:
                    path.append(st)
                    backtrack(i+1)
                    path.pop()
        
        backtrack()
        return res