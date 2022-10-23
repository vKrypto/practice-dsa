# https://leetcode.com/problems/maximum-number-of-balls-in-a-box/submissions/

class Solution(object):
    def get_digit_sum(self, num):
        """
        returns digits sum,
        i.e: 291 ==? 2+9+1 => 12
        """
        res = 0    
        while num:
            res += num%10
            num = num//10
        return res
        
    def countBalls_1(self, lowLimit, highLimit):
        """Runtime: 1673 ms, faster than 53.72% of Python online submissions for Maximum Number of Balls in a Box.
        -Memory Usage: 16.1 MB, less than 68.60% of Python online submissions for Maximum Number of Balls in a Box.
        : using map
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        dp = {}
        max_num = 0
        for i in range(lowLimit, highLimit+1):
            temp = self.get_digit_sum(i)
            dp[temp] = dp.get(temp, 0) + 1
            if max_num  < dp[temp]:
                max_num = dp[temp]
        return max_num
    
    def countBalls_2(self, lowLimit, highLimit):
        """
        Runtime: 1110 ms, faster than 73.56% of Python online submissions for Maximum Number of Balls in a Box.
        Memory Usage: 16 MB, less than 78.51% of Python online submissions for Maximum Number of Balls in a Box.
        : using list
        : time : o(nk) k== mx length of digit
        : space : theta(45+3)
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        dp = [0]*46
        max_num = 0
        for i in range(lowLimit, highLimit+1):
            temp = self.get_digit_sum(i)
            dp[temp] += 1
            if max_num  < dp[temp]:
                max_num = dp[temp]
        return max_num
    
    
    def countBalls_3(self, lowLimit, highLimit):
        """
        Runtime: 279 ms, faster than 100.00% of Python online submissions for Maximum Number of Balls in a Box.
        Memory Usage: 16.2 MB, less than 28.10% of Python online submissions for Maximum Number of Balls in a Box.: using dict
        : time : o(n)
        : space : theta(45+3)
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        Runtime: 255 ms, faster than 100.00% of Python online submissions for Maximum Number of Balls in a Box.
        Memory Usage: 16 MB, less than 78.51% of Python online submissions for Maximum Number of Balls in a Box.
        """
        box = {}
        digit_sum = self.get_digit_sum(lowLimit-1) # calcualte starting digit sum
        max_count = 0
        for i in range(lowLimit, highLimit + 1):
            while i % 10 == 0:
                i //= 10
                digit_sum -= 9
            digit_sum += 1
            box_number = digit_sum-1
            box[box_number] = box.get(box_number, 0) +1
            if box[box_number] > max_count:
                max_count = box[box_number]
        return max_count
    
    
    def countBalls(self, lowLimit, highLimit):
        """
        Runtime: 267 ms, faster than 100.00% of Python online submissions for Maximum Number of Balls in a Box.
        Memory Usage: 16.1 MB, less than 68.60% of Python online submissions for Maximum Number of Balls in a Box.
        : using list
        : time : o(n+k) k == len(lowerlimit)
        : space : theta(45+3)
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        Runtime: 255 ms, faster than 100.00% of Python online submissions for Maximum Number of Balls in a Box.
        Memory Usage: 16 MB, less than 78.51% of Python online submissions for Maximum Number of Balls in a Box.
        """
        box = [0] * 46 # max limit 10**5 ==> 99999 ==> 9*5
        digit_sum = self.get_digit_sum(lowLimit-1) # calcualte starting digit sum
        max_count = 0
        for i in range(lowLimit, highLimit + 1):
            while i % 10 == 0:
                i //= 10
                digit_sum -= 9
            digit_sum += 1
            box_number = digit_sum-1
            box[box_number] += 1
            if box[box_number] > max_count:
                max_count = box[box_number]
        return max_count
    