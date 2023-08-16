# coding: utf-8

"""
https://leetcode.com/problems/coin-change-ii/
"""
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
    
    def change(self, amount: int, coins: List[int]) -> int:
        g_coins_count =  float('inf')
        coins.sort(reverse=True)
        max_per_coins = [amount//i for i in coins]
        for coin_index in range(len(coins)):
            while max_per_coins[coin_index] > 0:
                temp_amount = amount
                coins_count = 0
                i = 0
                while temp_amount>0 and i <= len(coins)-1:
                    coin_used = min(max_per_coins[i], temp_amount//coins[i])
                    amount_remained = temp_amount - coin_used*coins[i]
                    print(coins[i], "X", coin_used, amount_remained)
                    coins_count += coin_used
                    temp_amount = amount_remained
                    i += 1
                if temp_amount:
                    print("not possible.")
                else:
                    print("coin used : ", coins_count)
                    g_coins_count = min(g_coins_count, coins_count)
                max_per_coins[coin_index] -= 1
            break
        return g_coins_count
    
    def change(self, amount: int, coins: List[int]) -> int: 
        n = len(coins)
        dp =[[0 for x in range(amount+1)] for x in range(n+1)]
        
        for i in range(n+1):
            dp[i][0]=1 
        
        # iterate over coins
        for i in range(1,n+1):
            # iterate over amounts
            for am in range(1,amount+1):
                dp[i][am]= dp[i-1][am]
                
                coin_val = coins[i-1]
                # if can include single instance of this coin
                if am >= coin_val:
                    dp[i][am] +=dp[i][am-coins[i-1]]
        
        return dp[n][amount]
    