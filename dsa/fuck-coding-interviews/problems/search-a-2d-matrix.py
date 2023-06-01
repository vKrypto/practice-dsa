# https://leetcode.com/problems/search-a-2d-matrix/submissions/945833567/
from . import List


class Solution:
    # time == o(log(mn)), space == o(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix),len(matrix[0])

        # step 1: find suitable row using binary search 
        i, j = 0, rows-1
        while i <= j:
            mid = (i+j)//2
            if target > matrix[mid][columns-1]:
                i = mid + 1
            elif target < matrix[mid][0]:
                j = mid - 1
            else:
                i = j = mid
                break
        target_row = mid

        # step 2: search within row matrix[target_row] using binary search
        i, j = 0, columns-1
        while i <= j:
            mid = (i+j)//2
            if target > matrix[target_row][mid]:
                i = mid + 1
            elif target < matrix[target_row][mid]:
                j = mid - 1
            else:
                return True
            
        return False
            