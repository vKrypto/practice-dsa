"""
https://leetcode.com/problems/longest-common-subsequence/description/
"""
import functools

class Solution:

    def __init__(self):
        self.memoized_results = {}

    def memoize(key_args):
        """
        A wrapper for memoization, caches response based on keyword arguments.
        """
        def wrapper(func):
            @functools.wraps(func)
            def wrapped_view(self, *args, **kwargs):
                key = "".join([str(kwargs.get(k, None)) for k in key_args])
                if key in self.memoized_results:
                    return self.memoized_results[key]
                else:
                    self.memoized_results[key] = func(self, *args, **kwargs)
                    return self.memoized_results[key]
            return wrapped_view

        return wrapper


    @memoize(key_args=['idx1', 'idx2'])
    def longestCommonSubsequence(self, text1: str, text2: str, idx1=0, idx2=0) -> int:
        # Terminating condition
        if idx1 == len(text1) or idx2 == len(text2):
            return 0
        
        if text1[idx1] == text2[idx2]:
            return 1 + self.longestCommonSubsequence(text1, text2, idx1=idx1+1, idx2=idx2 +1)
        else:
            return max(
                self.longestCommonSubsequence(text1, text2, idx1=idx1+1, idx2=idx2), 
                self.longestCommonSubsequence(text1, text2, idx1=idx1, idx2=idx2+1)
            )
            
    def longestCommonSubsequence_function(self, text1: str, text2: str, idx_1=0, idx_2=0) -> int:
        """
        using recursions is quite costly
        """
        key = (idx_1, idx_2)
        if key in self.memoized_results:
            return self.memoized_results[key]
        
        if idx_1 == len(text1) or idx_2 == len(text2):
            res = 0
        elif text1[idx_1] == text2[idx_2]:
            res = 1 + self.longestCommonSubsequence(text1, text2, idx_1+1, idx_2 +1)
        else:
            res = max(
                self.longestCommonSubsequence(text1, text2, idx_1+1, idx_2), 
                self.longestCommonSubsequence(text1, text2, idx_1, idx_2+1)
            )
        self.memoized_results[key] = res
        
        return self.memoized_results[key]
    
    def longestCommonSubsequence_dp(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        self.memoized_results = [[0] * (cols+1) for _ in range(rows+1)]

        for i, char1 in enumerate(text1, 1):
            for j, char2 in enumerate(text2, 1):
                if char1 == char2:
                    self.memoized_results[i][j] = self.memoized_results[i-1][j-1] + 1
                else:
                    self.memoized_results[i][j] = max(
                        self.memoized_results[i-1][j],
                        self.memoized_results[i][j-1]
                    )

        return self.memoized_results[rows][cols]
