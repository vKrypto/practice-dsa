# https://leetcode.com/problems/pacific-atlantic-water-flow/

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()
        dirs = [(1,0), (-1,0), (0, 1), (0, -1)]
        
        
        def dfs(i, j, visited, last_height=0):
            node_height = heights[i][j]
            if node_height < last_height:
                return 
            visited.add((i, j))
            for inc_i, inc_j in dirs:
                n_i = i+inc_i
                n_j = j+inc_j
                if 0 <= n_i < rows and 0 <= n_j < cols and (n_i, n_j) not in visited:
                    dfs(n_i, n_j, visited, node_height)
                    
        
        for row in range(rows):
            dfs(row, 0, pac, heights[row][0]) 
            dfs(row, cols-1, atl, heights[row][cols-1]) 
        
        for col in range(cols):
            dfs(0, col, pac, heights[0][col]) 
            dfs(rows-1, col, atl, heights[rows-1][col]) 

        res = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pac and (row, col) in atl:
                    res.append((row, col))

        return res