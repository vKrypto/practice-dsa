# https://leetcode.com/problems/length-of-last-word/submissions/


class Solution:
    """
    Runtime: 33 ms, faster than 90.66% of Python3 online submissions for Length of Last Word.
    Memory Usage: 13.9 MB, less than 80.12% of Python3 online submissions for Length of Last Word.
    """
    def lengthOfLastWord(self, s: str) -> int:
        for i in s.split(" ")[::-1]:
            if len(i) > 0:
                return len(i)
        return 0            

    """
    more language independent code
    """
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in s[::-1]:
            if i != ' ' and count == 0:
                count = 1
            elif i == ' ' and count != 0:
                return count
            elif i == ' ' and count == 0:
                pass
            else:
                count += 1
        return count
