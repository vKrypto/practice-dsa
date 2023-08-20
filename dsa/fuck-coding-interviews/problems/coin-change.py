# coding: utf-8
"""
https://leetcode.com/problems/coin-change/
"""
from itertools import combinations
from typing import List


# Time Limit Exceeded.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if min(coins) > amount:
            return -1

        # Generate all subsets.
        def build_subsets(items):
            subsets = set()
            for i in range(1, len(items) + 1):
                subsets |= set(combinations(items, i))
            return subsets

        items = []
        for coin in coins:
            max_n = amount // coin
            items.extend([coin, ] * max_n)

        min_n = float('inf')
        for result in build_subsets(items):
            n = len(result)
            if n > min_n:
                continue
            if sum(result) == amount:
                if n < min_n:
                    min_n = n

        if min_n == float('inf'):
            return -1
        else:
            return min_n


class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Numbers of coins for amount [0, ..., amount].
        coins_n = [float('inf'), ] * (amount + 1)
        coins_n[0] = 0

        for coin in coins:
            for current_amount in range(coin, amount + 1):  # [coin, ..., amount]
                # The number of coins before adding the current coin to it.
                previous_n = coins_n[current_amount - coin]
                current_n = previous_n + 1
                if coins_n[current_amount] > current_n:
                    coins_n[current_amount] = current_n

        if coins_n[amount] == float('inf'):
            return -1
        else:
            return coins_n[amount]


class Solution3:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Numbers of coins for amount [0, ..., amount].
        coins_n = [float('inf'), ] * (amount + 1)
        coins_n[0] = 0

        sorted_coins = sorted(coins)

        # Iterate every needed amount.
        for current_amount in range(1, amount + 1):
            for coin in sorted_coins:
                if coin > current_amount:
                    break

                # The number of coins before adding the current coin to it.
                previous_n = coins_n[current_amount - coin]
                # Add 1 of the current coin.
                current_n = previous_n + 1
                if coins_n[current_amount] > current_n:
                    coins_n[current_amount] = current_n

        if coins_n[amount] == float('inf'):
            return -1
        else:
            return coins_n[amount]

class Solution4:
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1]* (amount +1)
        dp[0] = 0
        
        for i in range(1, amount +1):
            for c in coins:
                # check amount can use at least on coins of amount c,
                if i - c >= 0:
                    dp[i] = min(dp[i], 1+dp[i-c])
                    
        return dp[amount] if dp[amount] != amount +1 else -1
    
    
    

class Solution5:
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        # greedy approach
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
            
        

class Solution6:
    
    # step 1: recursion solution
    def coinChange_1(self, coins: List[int], amount: int) -> int:
        def func(index):
            if index == 0:
                return 0
            coins_used = float('inf')
            for coin in coins:
                if coin <= index:
                    coins_used = min(coins_used, 1+ func(index-coin))
            return coins_used
        
        res = func(amount)
        return res if res != float('inf') else -1

    # step 1: recursion solution + add memoization    
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [None for _ in range(amount + 1)]

        def func(index):
            if index == 0:
                return 0
            if memo[index] is not None:
                return memo[index]
            coins_used = float('inf')
            for coin in coins:
                if coin <= index:
                    coins_used = min(coins_used, 1+ func(index-coin))
        
            return coins_used
        res = func(amount)
        return res if res != float('inf') else -1


    # step 1: convert into tabulation solution    
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [None for _ in range(amount + 1)]
        memo[0] = 0
        
        for index in range(1, amount+1):
            if memo[index] is not None:
                return memo[index]
            coins_used = float('inf')
            for coin in coins:
                if coin <= index:
                    coins_used = min(coins_used, 1+ memo[index-coin])
            memo[index] = coins_used

        res = memo[amount]
        return res if res != float('inf') else -1


Solution4().coinChange([1,5,7], 36)