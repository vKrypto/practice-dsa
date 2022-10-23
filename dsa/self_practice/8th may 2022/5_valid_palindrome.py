# https://leetcode.com/problems/valid-palindrome/
class Solution:
    """
    time complexity: O(N)
    Runtime: 57 ms, faster than 66.53% of Python3 online submissions for Valid Palindrome.
    Memory Usage: 14.4 MB, less than 86.17% of Python3 online submissions for Valid Palindrome.
    """
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if not (s[r].isalpha() or s[r].isdigit()):
                r -= 1
                continue
            if not (s[l].isalpha() or s[l].isdigit()):
                l += 1
                continue
                
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True