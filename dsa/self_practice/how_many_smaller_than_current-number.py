
class Solution:
    
        
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dup = sorted(nums)
        result = []
        for i in nums:
            temp_index = dup.index(i)
            while dup[temp_index] and temp_index > 0 and dup[temp_index-1] == dup[temp_index]:
                temp_index -= 1
            result.append(temp_index)
        return result
    
    # Runtime: 280 ms, faster than 47.41% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
    # Memory Usage: 13.9 MB, less than 86.14% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
    # time complexity: O(n*2 + nlogn ) and space complexity: O(2n)
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        result = []
        for i in nums:
            count = 0
            for j in temp:
                if j < i:
                    count += 1
                else:
                    break
            result.append(count)
        return result