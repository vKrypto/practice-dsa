from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        dirs = [(1,0), (-1,0), (0, 1), (0, -1)]
        visited = set()
        all_visited = set()
        
        def is_covered(i, j):
            # boundary crossed
            if not(0 <= i < rows and 0 <= j < cols):
                return False
            # found x 
            if board[i][j] == 'X':
                return True
            
            visited.add((i,j))
            all_visited.add((i,j))
            all_covered = True 
            
            for inc_i, inc_j in dirs:
                child_i = i+inc_i
                child_j = j + inc_j
                if (child_i, child_j) not in all_visited:
                    if not is_covered(child_i, child_j):
                        all_covered = False
            
            return all_covered


        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i, j) not in all_visited :
                    visited = set()
                    if is_covered(i,j):
                        for (x,y) in visited:
                            board[x][y] = "X"
        print(board)

class Solution2:
   def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # 1. (DFS) Capture bordered regions (O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    capture(r, c)

        # 2. Capture surrounded regions (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. Uncaptured modified regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
        
        
board = [["O","X","O"],["X","O","X"],["O","X","O"]]

# board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Solution2().solve(board)