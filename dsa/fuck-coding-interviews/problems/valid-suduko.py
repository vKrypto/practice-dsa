# https://leetcode.com/problems/valid-sudoku/

from typing import List
from collections import defaultdict

class Solution:

    """
    more readable code, iterate only once for a number
    Runtime: 97 ms, faster than 88.31% of Python3 online submissions for Valid Sudoku.
    Memory Usage: 13.8 MB, less than 99.09% of Python3 online submissions for Valid Sudoku.
    """
    def isValidSudoku_1(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        sub_set = defaultdict(set)
        for i, row in enumerate(board):
            for j, item in enumerate(row):
                if item == ".":
                    continue
                if (item in row_set[i] or item in col_set[j] or item in sub_set[(i//3, j//3)]):
                    return False
                row_set[i].add(item)
                col_set[j].add(item)
                sub_set[(i//3, j//3)].add(item)
        return True



    """
    Runtime: 98 ms, faster than 87.18% of Python3 online submissions for Valid Sudoku.
    Memory Usage: 13.9 MB, less than 84.01% of Python3 online submissions for Valid Sudoku.
    """
    def is_valid_list(self, nums:List[str]) -> bool:
        dp = {}
        for i in nums:
            if i != ".":
                if dp.get(i) is not None:
                    return False
                dp[i] = 1
        return True
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_n, col_n = len(board), len(board[0])
        # check rows,
        for i in range(row_n):
            if not self.is_valid_list(board[i]):
                print("failed row ", board[i])
                return False

        # check columns
        for i in range(col_n):
            row =  [board[j][i] for j in range(row_n)]
            if not self.is_valid_list(row):
                print("failed col ", row)
                return False
        
        
        # check sub box
        sub_size = 3
        for i in range(row_n//sub_size):
            for j in range(col_n//sub_size):
                dp = {}
                for k in range(sub_size):
                    for l in range(sub_size):
                        item = board[i*sub_size+k][j*sub_size+l]
                        if item != ".":
                            if dp.get(item) is not None:
                                print("fialed sub box", [i, j], " elem: ", [k,l] )
                                return False
                            dp[item] = 1

        return True