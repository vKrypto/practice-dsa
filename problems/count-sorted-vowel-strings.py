# https://leetcode.com/problems/count-sorted-vowel-strings/submissions/


class Solution:
    # recursion witb caching
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5

        cache = {(1,0):5}
        def rec(n, last_char=0):
            # add-caching
            if (n, last_char) in cache:
                return cache[(n, last_char)]
            # base-case.
            if n == 1:
                return 5 - last_char + 1
            
            # index-case
            res_count = 0
            for i in [1, 2, 3, 4, 5]:
                if last_char <= i:
                    res_count += rec(n-1, last_char=i)
            cache[(n,last_char)] = res_count
            return res_count
            
        x = rec(n)
        return x


    # recusion with dp
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5
            
        dp = [[None]*6 for _ in range(n+1)]
        def rec(n, last_char=0):
            # add-caching
            if dp[n][last_char] is not None:
                return dp[n][last_char]
            # base-case.
            if n == 1:
                return 5 - last_char + 1
            
            # index-case
            res_count = 0
            for i in [1, 2, 3, 4, 5]:
                if last_char <= i:
                    res_count += rec(n-1, last_char=i)
            dp[n][last_char] = res_count
            return res_count
            
        x = rec(n)
        return x

    def countVowelStrings(self, n: int) -> int:
        dp = [[None]*5 for _ in range(n)]
        # base-case.
        for last_char in range(5):
            dp[0][last_char] = 5 - last_char
        
        # index-case
        for i in range(1, n):
            for last_char in range(5):
                res_count = 0
                for char in range(5):
                    if last_char <= char:
                        res_count += dp[i-1][char]
                dp[i][last_char] = res_count
        print(dp)
        return dp[n-1][0]
    
    def countVowelStrings(self, n: int) -> int:
        # base-case.
        prev = [5-i for i in range(5)]
        cur = [None for _ in range(5)]
        
        # index-case
        for i in range(1, n):
            for last_char in range(5):
                res_count = 0
                for char in range(5):
                    if last_char <= char:
                        res_count += prev[char]
                cur[last_char] = res_count
            prev = cur
        return prev[0]
print(Solution().countVowelStrings(3))