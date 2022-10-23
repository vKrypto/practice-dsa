# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/submissions/
from typing import List

class Solution:
    #Runtime: 57 ms, faster than 87.76% of Python3 online submissions for Final Value of Variable After Performing Operations.
    # Memory Usage: 13.8 MB, less than 96.64% of Python3 online submissions for Final Value of Variable After Performing Operations.
    # time Complexity: O(n) and space Complexity: O(1)
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x= 0
        for i in operations:
            if "--" in i:
                x -= 1
            else:
                x += 1
        return x