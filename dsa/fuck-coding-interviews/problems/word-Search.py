'''Leetcode- https://leetcode.com/problems/word-search/'''
'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
'''
from . import List
from itertools import product, starmap


# Solution
def exist(board, word):
    ROWS, COLS = len(board), len(board[0])
    path = set()

    def dfs(r, c, i):
        if i == len(word):
            return True
        if (r < 0 or c < 0 or
            r >= ROWS or c >= COLS or
            word[i] != board[r][c] or
                (r, c) in path):
            return False

        path.add((r, c))
        res = (dfs(r+1, c, i+1) or
               dfs(r-1, c, i+1) or
               dfs(r, c+1, i+1) or
               dfs(r, c-1, i+1))
        path.remove((r, c))
        return res

    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0):
                return True
    return False

#T: O(n*m*4^n)
#S: O(n)




class Solution:
    # O(n * m * 4^n)
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        paths = set()
        word_length = len(word)
        if word_length > rows * cols:
            return False

        def dfs(row_index:int, col_index:int, target_index:int):
            # True if words finished
            if target_index == word_length:
                return True
            # False if out of bound for board
            if (row_index < 0 or col_index < 0 or row_index >= rows or col_index>=cols):
                return False
            
            # if word not matched or already used.
            char = board[row_index][col_index]
            if char != word[target_index] or (row_index, col_index) in paths:
                return False

            
            # found matching word
            paths.add((row_index, col_index))

            # scan horizantly, vertically for next word
            res = (
                dfs(row_index-1, col_index, target_index+1) or
                dfs(row_index+1, col_index, target_index+1) or
                dfs(row_index, col_index-1, target_index+1) or
                dfs(row_index, col_index+1, target_index+1)
            )
            paths.remove((row_index, col_index))
            return res

        
        # search for starting word.
        for row_index in range(rows):
            for col_index in range(cols):
                res = dfs(row_index, col_index, 0)
                if res:
                    return True
        
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m, wrdlen = len(board), len(board[0]), len(word)
        if wrdlen > m * n:
            return False

        def dfs(r, c, i=0) -> bool:
            if board[r][c] != word[i]:
                return False
            if i == wrdlen - 1:
                return True
            
            board[r][c] = "#"
            i += 1
            valid = (
                (r > 0 and dfs(r - 1, c, i))
                or (r < n - 1 and dfs(r + 1, c, i))
                or (c > 0 and dfs(r, c - 1, i))
                or (c < m - 1 and dfs(r, c + 1, i))
            )
            board[r][c] = word[i - 1]
            return valid

        cnts = [0] * 58
        for r, c in product(range(n), range(m)):
            cnts[ord(board[r][c]) - ord("A")] += 1
        if cnts[ord(word[0]) - ord("A")] > cnts[ord(word[-1]) - ord("A")]:
            word = word[::-1]
        return any(starmap(dfs, product(range(n), range(m))))