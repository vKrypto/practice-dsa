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


class Solution2:
    def __input_optimization(self, wordDict):
        # optimization 1: remove super set values
        l_set = set(wordDict)
        n_max = max([len(i) for i in wordDict])
        for i in wordDict:
            if i not in l_set:
                continue
            count = 2
            while len(i)* count <= n_max:
                temp = i * count
                if temp in l_set:
                    l_set.remove(temp)
                count += 1
        # optimization 2: try big size str first
        wordDict = list(l_set)
        wordDict.sort(key=len, reverse=True)
        return wordDict

    def wordBreak_rec(self, s: str, wordDict: List[str]) -> bool:
        wordDict = self.__input_optimization(wordDict) 
        # brute force + recursion + memo
        memo = {"": True}

        def rec(s):
            if s in memo:
                return memo[s]
            for word in wordDict:
                n = len(word)
                if word == s[:n]:
                    if rec(s[n:]):
                        memo[s] = True
                        return memo[s]
            memo[s] = False
        return rec(s)

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = self.__input_optimization(wordDict) 

        # dp + base-case
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                n = len(w)
                if w[0] == s[i] and w == s[i:i+n] and dp[n+i]:
                    dp[i] = True
        return dp[0]

    