# https://leetcode.com/problems/count-servers-that-communicate/submissions/
from typing import List

class Solution:
    def check_for_a_server(self, grid, i, j):
        """
        time: o(i*j)
        space: o(1)
        """
        for row in range(self.row_len):
            if row != i:
                val = grid[row][j]
                if val:
                    return True
        for col in range(self.col_len):
            if col != j:
                val = grid[i][col]
                if val:
                    return True
        return False
        
    def countServers(self, grid: List[List[int]]) -> int:
        """
        time: o((i*j)^2)
        space: o(i*j)
        Runtime: 522 ms, faster than 89.86% of Python3 online submissions for Count Servers that Communicate.
        Memory Usage: 15.6 MB, less than 89.86% of Python3 online submissions for Count Servers that Communicate.
        """
        self.row_len = len(grid)
        self.col_len = len(grid[0])
        total_server = 0
        for row in range(len(grid)):
            any_server_in_row = False
            for col in range(len(grid[row])):
                val = grid[row][col]
                if val:
                    any_server_in_row = self.check_for_a_server(grid, row, col)
                    if any_server_in_row:
                        total_server += 1
                    else:
                        break
        return total_server