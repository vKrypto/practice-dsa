

class Solution:
    
    # recursive solution
    def longestPalindrome_1(self, s: str) -> str:
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

    # iterate solution
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res