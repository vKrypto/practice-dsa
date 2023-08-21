# https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/description/


# bijection method : total number of at least one collision = total number of moves - moves with no collision

class Solution:
    def monkeyMove(self, n: int) -> int:
        res = 2**n -2
        return res%100000007

    def monkeyMove(self, n: int) -> int:
        modulo = 1_000_000_007
        answer = 1
        exponent = 2
        while n:
            if n&1:
                answer *= exponent                
            exponent = (exponent*exponent) % modulo
            n >>= 1
        answer += modulo - 2
        answer %= modulo      
        return answer