# https://leetcode.com/problems/number-of-islands/description/

from typing import List

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        col, row = len(grid), len(grid[0])
        visited = set()
        
        # def dfs(i, j):
        #     try:
        #         if grid[i][j] == '0' or (i,j) in visited:
        #             return
        #     except:
        #         return

        #     visited.add((i, j))   
        #     dfs(i-1, j)  # check left
        #     dfs(i+1, j)  # check right 
        #     dfs(i, j-1)  # check up
        #     dfs(i, j+1)  # check down
        
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def helper(c: int, r: int):
            try:
                if grid[c][r] == '0':
                    return
            except:
                return

            visited.add((c, r))

            for i, j in dir:
                nc, nr = c+i, r+j
                if 0 <= nc < col and 0 <= nr < row and (nc, nr) not in visited:
                    helper(nc, nr)

        res = 0
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] == '1':
                    helper(i, j)
                    res += 1
        return res

