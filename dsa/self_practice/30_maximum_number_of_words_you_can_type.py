# https://leetcode.com/problems/maximum-number-of-words-you-can-type/submissions/

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """
        paatern: bruteforrce
        time: o(n*2)
        space: o(1)
        Runtime: 38 ms, faster than 88.03% of Python3 online submissions for Maximum Number of Words You Can Type.
        Memory Usage: 14 MB, less than 25.86% of Python3 online submissions for Maximum Number of Words You Can Type.
        """
        count = 0
        for word in text.split(" "):
            matched = False
            for letter in brokenLetters:
                if letter in word:
                    matched = True
                    break
            if not matched:
                count += 1
        return count