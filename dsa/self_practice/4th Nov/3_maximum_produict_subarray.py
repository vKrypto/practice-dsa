# https://leetcode.com/problems/maximum-product-subarray
class Solution:
    """
    pattern: maintain g_max, g_min at the same time and reset to 1 when num ==0
    Runtime: 91 ms, faster than 91.38% of Python3 online submissions for Maximum Product Subarray.
    Memory Usage: 14.4 MB, less than 38.05% of Python3 online submissions for Maximum Product Subarray.
    """
    def maxProduct(self, nums: List[int]) -> int:
        g_max_product = 1
        g_min_product =  1
        res = max(nums)
        
        for i in nums:
            if i == 0:
                g_max_product = 1
                g_min_product =  1
                continue
            g_max_product, g_min_product = max(g_max_product *i,g_min_product * i, i), min(g_max_product *i,g_min_product * i, i)
            res = max(res, g_max_product)
        return res