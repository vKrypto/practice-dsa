# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    """
    time complexity: O(3n)
    space compelexity: O(3n)
    Runtime: 589 ms, faster than 18.93% of Python3 online submissions for Product of Array Except Self. 
    Memory Usage: 22.4 MB, less than 24.11% of Python3 online submissions for Product of Array Except Self.
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        
        from_end = [1] * n
        curr = 1
        for i in range(n-1, -1, -1):
            from_end[i] = curr
            curr *= nums[i] 
            
        
        from_start = [1] * n
        curr = 1
        for i in range(n):
            from_start[i] = curr
            curr *= nums[i] 
            
        output = []
        for i in range(n):
            output.append(from_start[i] * from_end[i])
        
        return output

    """
    time complexity: O(2n)
    space compelexity: O(n)
    Runtime: 450 ms, faster than 43.37% of Python3 online submissions for Product of Array Except Self.
    Memory Usage: 21.2 MB, less than 81.94% of Python3 online submissions for Product of Array Except Self.
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        
        output = [1] * n
        curr = 1
        for i in range(n-1, -1, -1):
            output[i] = curr
            curr *= nums[i] 
            
        curr = 1
        for i in range(n):
            output[i] *= curr
            curr *= nums[i] 
            
        return output
            