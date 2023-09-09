# https://leetcode.com/problems/number-of-islands/description/

from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        col, row = len(grid), len(grid[0])
        visited = set()
        

        def dfs(c: int, r: int):
            # this statement should not be required.
            # if not(0 <= c < col and 0 <= r < row and (c,r)):
            #     return
            try:
                if grid[c][r] == '0' or (c,r) in visited:
                    return
            except IndexError:
                return
            visited.add((c, r))

            dfs(c-1, r)  # check left
            dfs(c+1, r)  # check right 
            dfs(c, r-1)  # check up
            dfs(c, r+1)  # check down
        
        res = 0
        for i in range(col):
            for j in range(row):
                if (i,j) not in visited and grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        return res

