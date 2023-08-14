# coding: utf-8

"""
https://leetcode.com/problems/coin-change-ii/
"""
from itertools import combinations
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int: 
        # recursive solution

        def rec(amount_remained=amount, index=len(coins)-1):
            if index < 0 or amount_remained < 0:
                return 0
            if amount_remained==0:
                return 1
            include_coin = rec(amount_remained-coins[index], index) 
            not_include_coin = rec(amount_remained, index-1)
            return not_include_coin + include_coin

        return rec()