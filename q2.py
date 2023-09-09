"""
This problem was asked by Twitter.

Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer.

For example, given [10, 7, 76, 415], you should return 77641510.

"""
from typing import List


class Solution:
    def reOrder_1(self, nums:List):
        # pattern: lexicographical order, in reverse
        # using builtin funciton
        # time complexity:  o(nlogn)
        # space compelxity: o(1)
        nums.sort(key=str, reverse=True)
        print(nums)

    def reOrder(self, x:List):
        # for i, v1 in enumerate(nums):
        #     print(v1, nums)
        #     for j, v2 in enumerate(nums[i+1:]):
        #         if str(v1) < str(v2):
        #             nums[i], nums[j] = nums[j], nums[i]
        loops, swaps = 0, 0
        # random.shuffle(x)
        # -----------------------------
        for i in range(len(x)-1):
            swap = 0
            # find biggest and move to end.
            for j in range(len(x)-i-1):
                loops += 1
                if str(x[j]) > str(x[j+1]):
                    swaps += 1
                    swap += 1
                    x[j], x[j+1] = x[j+1], x[j]
            if not swap:
                break
        print(x[::-1])




tests = [
   [10, 7, 76, 415, 3, 2, 4, 5,12,145,98] 
]

outputs = [
   [76, 7, 415, 10] 
]

for i, test in enumerate(tests):
    Solution().reOrder(test)