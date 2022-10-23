# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/



class Solution:
    # Runtime: 53 ms, faster than 71.92% of Python3 online submissions for Kids With the Greatest Number of Candies.
    # Memory Usage: 13.9 MB, less than 63.44% of Python3 online submissions for Kids With the Greatest Number of Candies.
    # time Complexity: O(2n) and space Complexity: O(1)
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        temp = max_candies - extraCandies
        return [i > temp or i == temp for i in candies]
