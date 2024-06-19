# https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even = [0, 2, 4, 6, 8]
        prime = [2, 3, 5, 7]
        res = [] # repr for str number

        def rec(i):
            # base case:
            if i < 0:
                return 1
            ls = prime if i % 2 else even
            ans = 0
            for j in ls:
                res.append(j)
                ans += rec(i-1)
                res.pop()
            
            return ans

        return rec(n)



print(Solution().countGoodNumbers(3))