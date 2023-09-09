class Solution:

    def myPow_recursive(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            if x ==1 or x ==-1:
                if n % 2 == 0:
                    return abs(x)
                else:
                    return x

            res = helper(x * x, n // 2)
            return x * res if n % 2 else res

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res

    def myPow_iterative(self, x: float, n: int) -> float:
        # base-condition
        if n==0:
            return 1
        is_negative = n < 0
        n = abs(n)
    
        i, result =1, x
        while i*2 < n:
            i = i*2 
            result *= result
        result *= self.myPow(x, n-i)
        return result if not is_negative else 1/result

    # time: o(logn), space: o(logn)
    def myPow_optimized(self, x: float, n: int) -> float:
        # base-condition
        is_negative = n < 0
        n = abs(n)
        if n==0:
            return 1
        if n == 1:
            return x if not is_negative else 1/x
        if x ==1 or x ==-1:
            if n % 2 == 0:
                return abs(x)
            else:
                return x
                
            
        def _get_closest_match(i, keys):
            last_key = None
            for key in keys:
                if i < key:
                    break
                last_key = key
            return last_key

        # memoizing time: o(logn), space: o(logn)
        dp = {1: x}
        result = x
        i = 1
        while i*2 < n:
            i = i*2 
            result *= result
            dp[i] = result

        # time: o(logn), space: o(logn)
        remaing_pow = n-i
        while remaing_pow:
            if remaing_pow in dp:
                result *= dp[remaing_pow]
                break

            closest_match = _get_closest_match(remaing_pow, dp.keys())
            if closest_match:
                remaing_pow -= closest_match
                result *= dp[closest_match]
            else:
                break

        return result if not is_negative else 1/result

