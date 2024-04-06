# https://leetcode.com/problems/harshad-number/description/

class Solution:
    def sumOfTheDigitsOfHarshadNumber_1(self, x: int) -> int:
        y = sum([int(i) for i in str(x)])
        return -1 if x % y else y
        
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        x1 = x
        y = 0
        while x:
            x, temp = x//10, x%10
            y += temp
        return -1 if x1 % y else y