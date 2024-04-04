

class Solution:
    
    # recursive solution
    def longestPalindrome(self, s: str) -> str:
        res = [s[0], 1] # char, count
        n = len(s)

        def rec(left, right):
            nonlocal res
            # out of bound condition
            if (left < 0 or right >= n):
                return
            # not-valid condition
            if s[left] != s[right]:
                return
            # do the stuff.
            if res[1] < right-left+1:
                res = [s[left:right+1], right-left+1]
            rec(left-1, right+1)

        
        for i in range(len(s)):
            rec(i, i+1)  # odd length case
            rec(i-1, i+1) # even length case.

        return res[0]