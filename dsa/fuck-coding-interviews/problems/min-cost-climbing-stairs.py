# https://leetcode.com/problems/min-cost-climbing-stairs/description/
from typing import List


class Solution:

    # time: o(n), space: o(n)
    def minCostClimbingStairs_1(self, cost: List[int]) -> int:
        if len(cost) < 2:
            return 0
        cost_from_index = {len(cost)-1: cost[-1]}
        
        def dfs(index=0):
            if index > len(cost)-1:
                return 0
            elif index in cost_from_index:
                return cost_from_index[index]
            cost_from_index[index] = cost[index] + min(dfs(index+1), dfs(index+2))
            return cost_from_index[index]

        dfs()

        return min(cost_from_index[0], cost_from_index[1])

    # time: O(n), space:o(1), writes: o(n)
    def minCostClimbingStairs_2(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])

    # time: O(n), space:o(1), writes: o(1) # 99% faster
    def minCostClimbingStairs_3(self, cost: List[int]) -> int:
        first, second = cost[-2], cost[-1]
        for i in range(len(cost) - 3, -1, -1):
            first, second = cost[i] + min(first , second), first
        return min(first, second)
            