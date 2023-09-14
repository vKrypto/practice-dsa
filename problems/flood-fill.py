# https://leetcode.com/problems/flood-fill/

from typing import List


# Time Complexity : O(n*m)
# Space Complexity : O(n*m)
class Solution(object):
        
    def floodFill(self, image, sr, sc, color):
        # Avoid infinite loop if the new and old colors are the same...
        if image[sr][sc] == color:
            return image
        
        
        def dfs_fill(self, image, sr, sc, color, cur):
            # invalid cases
            if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
                return
            # If image[sr][sc] is not equal to previous color...
            if cur != image[sr][sc]:
                return
            image[sr][sc] = color

            dfs_fill(image, sr-1, sc, color, cur)
            dfs_fill(image, sr+1, sc, color, cur)
            dfs_fill(image, sr, sc-1, color, cur)
            dfs_fill(image, sr, sc+1, color, cur)

        dfs_fill(image, sr, sc, color, image[sr][sc])
        return image
    

class Solution2:
    def floodFill(self, image: List[List[int]], sr1: int, sc1: int, color1: int) -> List[List[int]]:
        followColor = image[sr1][sc1]
        row_c = len(image)
        col_c = len(image[0])
        visited = set()
        def dfs(i,j):
            if (
                i< 0 or i >=row_c
                or j<0 or j >= col_c
                or image[i][j] not in [followColor, None]
                or (i,j) in visited
                ):
                return
            
            image[i][j] =  None
            visited.add((i,j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        
        dfs(sr1, sc1)

        for i in range(row_c):
            for j in range(col_c):
                if image[i][j] == None:
                    image[i][j] =color1
        return image