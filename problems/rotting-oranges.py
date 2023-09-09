# https://leetcode.com/problems/rotting-oranges/


from typing import List
from collections import deque


class Solution:
    # time: 96%, space: 62% 
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        level_rotten = deque()
        total_tomato = 0
        # total number of fresh oranges, rotten_oranges at time=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    level_rotten.append((i,j))
                elif grid[i][j] == 1:
                    total_tomato += 1

        if not total_tomato:
            return 0       

        timer = 0
        dirs = [(1,0), (-1,0), (0, 1), (0,-1)]  
        rotted = 0
        # do a bfs for rotten
        while level_rotten:
            timer += 1
            length = len(level_rotten)
            for i in range(length):
                i,j = level_rotten.popleft()
                for x, y in dirs:
                    n_i, n_j = i + x, j + y
                    if (
                        0 <= n_i < rows and 0 <= n_j < cols 
                        and grid[n_i][n_j] == 1
                    ):
                        grid[n_i][n_j] = 2
                        rotted += 1
                        level_rotten.append((n_i, n_j))
        if total_tomato != rotted:
            return  -1
        return timer-1