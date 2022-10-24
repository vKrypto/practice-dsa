# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List, overload
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters = [
            None,
            None,
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]
        iterables = [letters[int(n)] for n in digits]
        return [''.join(x) for x in product(*iterables)] 