# https://leetcode.com/problems/01-matrix/description/

from collections import deque
from typing import List
import time


class Solution:
    # returns TLE
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        dirs = [
            (1,0), (-1,0), 
            (0, 1), (0,-1), 
        ]
        
        def bfs(i,j):
            queue_stack.append((i,j))

            loop = 0
            while queue_stack:
                loop += 1
                cur_len = len(queue_stack)
                for i in range(cur_len):
                    i, j = queue_stack.popleft()
                    for x, y in dirs:
                        x += i
                        y += j
                        if 0 <= x < rows and 0<= y < cols and (x, y) not in visited:
                            if mat[x][y] == 0:
                                return loop
                            visited.add((x,y))
                            queue_stack.append((x,y))
            return loop


        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 1:
                    queue_stack = deque()
                    visited = set()
                    # modifying matrix should not affect to response
                    # just need to careful while bfs                    
                    mat[row][col] = bfs(row, col) 
        return mat
        
        


class Solution2:
    
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        dirs = [
            (1,0), (-1,0), 
            (0, 1), (0,-1), 
        ]
        
        def bfs(i,j):
            queue_stack.append((i,j))

            loop = 0
            while queue_stack:
                # print("=========", queue_stack)
                loop += 1
                cur_len = len(queue_stack)
                for _ in range(cur_len):
                    cur_i, cur_j = queue_stack.popleft()
                    if mat[cur_i][cur_j] != 1:
                        mat[cur_i][cur_j] = min(mat[cur_i][cur_j], loop)
                    else:
                        mat[cur_i][cur_j] = loop
                    for x, y in dirs:
                        x += cur_i
                        y += cur_j
                        if 0 <= x < rows and 0<= y < cols and (x, y) not in visited:
                            if mat[x][y] != 0:
                                visited.add((x,y))
                                queue_stack.append((x,y))
            return loop


        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue_stack = deque()
                    visited = set()
                    # modifying matrix should not affect to response
                    # just need to careful while bfs   
                    print("crawkling", (row,col))                 
                    bfs(row, col) 
        return mat
    
num =  100
mat = [[1 for _ in range(num)] for _ in range(num)]
mat[-1][-1] = 0
print("Executing....")
begin = time.time()
Solution().updateMatrix(mat)
end = time.time()
print(mat)
# total time taken
print(f"Total runtime of the program is {end - begin}")



mat = [[1 for _ in range(num)] for _ in range(num)]
mat[-1][-1] = 0

print("Executing....")
begin = time.time()
Solution2().updateMatrix(mat)
end = time.time()
 
# total time taken
print(f"Total runtime of the program is {end - begin}")