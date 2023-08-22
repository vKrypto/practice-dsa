

class Solution:
    # recursive bottom up solution
    def uniquePaths(self, m: int, n: int) -> int:
        def rec(i,j):
            if i >= m or j >= n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            way_1 = rec(i+1, j)
            way_2 = rec(i, j+1)
            return way_1 + way_2
        return rec(0, 0)


    # recursive bottom up solution with caching
    def uniquePaths_1(self, m: int, n: int) -> int:
        cache = {(m-1,n-1): 1}

        def rec(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i >= m or j >= n:
                return 0
            way_1 = rec(i+1, j)
            way_2 = rec(i, j+1)
            cache[(i,j)] = way_1 + way_2
            return way_1 + way_2

        return rec(0, 0)

    # Beats 95.70% Space, Beats 95.67% runtime solution
    # time: o(m*n), space: o(m*n)
    # tabular bottom up solution    
    def uniquePaths_2(self, m: int, n: int) -> int:
        # step 1; initialize matrix
        dp = [[None for _ in range(n)] for _ in range(m)]
        # step2: add base-case.
        dp[-1][-1] = 1
        for i in range(n):
            dp[-1][i] = 1
        for i in range(m):
            dp[i][-1] = 1


        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]

    # top down cached recursive solution
    def uniquePaths_3(self, m: int, n: int) -> int:
        cache = {(0,0): 1}
        def rec(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i < 0 or j < 0:
                return 0

            cache[(i,j)] = rec(i-1, j) + rec(i, j-1)
            return cache[(i,j)]
        
        rec(m,n)
        return cache[(m-1, n-1)]