# https://leetcode.com/problems/verifying-an-alien-dictionary/

from typing import List
from itertools import chain, starmap,pairwise, dropwhile, zip_longest
from operator import eq



class Solution:
    def isAlienSorted_1(self, words: list[str], order: str) -> bool:
        EMPTY = ""
        ordinals = {ch: i for i, ch in enumerate(chain((EMPTY,), order))}

        def is_lexico(s1: str, s2: str) -> bool:
            pairs = zip_longest(s1, s2, fillvalue=EMPTY)
            ch1, ch2 = next(dropwhile(lambda chs: eq(*chs), pairs), (EMPTY, "z"))
            return ordinals[ch1] < ordinals[ch2]
        
        return all(starmap(is_lexico, pairwise(words)))

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        h = {ch: i for i, ch in enumerate(order)}
        prev = list(h[ch] for ch in words[0])
        for i in range(1, len(words)):
            cur = list(h[ch] for ch in words[i])
            if cur < prev:
                return False
            prev = cur
        return True
