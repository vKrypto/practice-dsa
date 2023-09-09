# https://leetcode.com/problems/word-break/submissions/

from typing import List


class Solution:
    # recursion with approach 1
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        cache = {}
        
        def func(l=0,r=1):
            if r >= len(s):
                return s[l:r+1] in wordDict
            if (l, r) in cache:
                return cache[(l,r)]
            case_1 = False
            # not take r if s[l:r] in dict
            if s[l:r] in wordDict:
                if r == len(s):
                    case_1 = True
                if func(r, r+1):
                    case_1 = True
            case_2 = func(l, r+1)
            cache[(l,r)] = case_1 or case_2
            return case_1 or case_2
        return func()
    
    
    # cached recursion with approach 2 
    def wordBreak_1(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        wordDict.sort(reverse=True)
        def rec(i=0):
            if i > len(s)-1:
                return True
            if i in cache:
                return cache[i]
            for word in wordDict:
                if word[0] == s[i]:
                    if word == s[i:i+len(word)]:
                        if rec(i+len(word)):
                            return True
            cache[i] = False
            return False
        return rec()
    
    def wordBreak_2(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if ((i + len(w)) <= len(s)
                    and s[i] == w[0]
                    and s[i : i + len(w)] == w
                ):
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]
