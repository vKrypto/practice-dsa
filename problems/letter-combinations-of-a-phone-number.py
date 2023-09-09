# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/


from typing import List
from itertools import product


class Solution:
    def __init__(self):
        self.letters = [
            0,
            0,
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]
        
    def letterCombinations(self, digits: str) -> List[str]:
        # base condition
        if not digits:
            return []
        
        res, path_set = [], []

        def backtrack(i=0):
            # base-condition
            if i == len(digits):
                res.append("".join(path_set))
                return
            
            for char in self.letters[int(digits[i])]:
                path_set.append(char)
                backtrack(i+1)
                path_set.pop()

        backtrack()
        return res

    def letterCombinations_2(self, digits: str) -> List[str]:
        if not digits:
            return []
        iterables = [self.letters[int(n)] for n in digits]
        return [''.join(x) for x in product(*iterables)] 
