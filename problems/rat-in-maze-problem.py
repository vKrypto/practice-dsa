"""
https://www.geeksforgeeks.org/rat-in-a-maze/
Consider a rat placed at (0, 0) in a square matrix of order N * N. 
It has to reach the destination at (N – 1, N – 1). 
Find all possible paths that the rat can take to reach from source to destination. 
The directions in which the rat can move are ‘U'(up), ‘D'(down), ‘L’ (left), ‘R’ (right).
Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it 
while value 1 at a cell in the matrix represents that rat can be travel through it.
Return the list of paths in lexicographically increasing order.

Note: In a path, no cell can be visited more than one time. 
If the source cell is 0, the rat cannot move to any other cell.
"""

maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]


class Solution:
    
    def num_of_ways(self, maze):
        i, j = 0, 0
        # base case
        if maze[i][j] == 0:
            return []
        
        n = len(maze)
        res = []
        path = []
        visited = [[False for _ in range(n)] for _ in range(n)]
        
        def backtrack(i, j):
            if i == n-1 and j == n-1:
                res.append(path[:])
                print(path)
                return
            if visited[i][j]:
                return
            visited[i][j] = True
            # up
            if i-1 >= 0 and maze[i-1][j] == 1:
                path.append("U")
                backtrack(i-1, j)
                path.pop()
            
            # down
            if i+1 < n and maze[i+1][j] == 1:
                path.append("D")
                backtrack(i+1, j)
                path.pop()
            
            # left
            if j-1 >= 0 and maze[i][j-1] == 1:
                path.append("L")
                backtrack(i, j-1)
                path.pop()
            
            # right
            if j+1 < n and maze[i][j+1] == 1:
                path.append("R")
                backtrack(i, j+1)
                path.pop()
            
        backtrack(0, 0)
        print(res)
        

Solution().num_of_ways(maze)