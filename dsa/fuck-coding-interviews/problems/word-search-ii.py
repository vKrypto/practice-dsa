from itertools import product, starmap
from typing import List

class Solution:
    
    # time: O(n * m * 4^n). space: O(n)
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m, wrdlen = len(board), len(board[0]), len(word)
        if wrdlen > m * n:
            return False

        def dfs(r, c, i=0) -> bool:
            if board[r][c] != word[i]:
                return False
            if i == wrdlen - 1:
                return True,
            
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
    
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        output = []
        for word in words:
            if self.exist(board, word):
                output.append(word)
        return output
