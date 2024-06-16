# https://leetcode.com/problems/n-queens/description/
from typing import List


class Solution:
    
    # time: o(2^n), space: o(n*n)
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        cols = [False for _ in range(n)]
        upper_diag = [False for _ in range(2*n)]
        lower_diag = [False for _ in range(2*n)]

        res = []
        def backtrack(row):
            # base-case
            if row == n:
                res.append(["".join(row) for row in board])
                return
            
            # fill col-by-col recursively
            for col in range(n):
                if (
                    not cols[col] and # cond1: same column
                    not upper_diag[row+col]and  # cond2: same upper diagonal
                    not lower_diag[row-col]  # cond3: same lower diagonal
                ):
                    cols[col] = True 
                    upper_diag[row+col] = True
                    lower_diag[row-col] = True
                    board[row][col] = "Q"
                    backtrack(row+1)
                    board[row][col] = "."
                    cols[col] = False 
                    upper_diag[row+col] = False
                    lower_diag[row-col] = False
                    
        backtrack(0)
        return res
                    