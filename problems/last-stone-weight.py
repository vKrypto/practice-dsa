# https://leetcode.com/problems/last-stone-weight/description/
import heapq
from typinf import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        stone_heap = [-i for i in stones]
        heapq.heapify(stone_heap)

        while len(stone_heap) > 1:
            first_max = heapq.heappop(stone_heap) # -3
            second_max = heapq.heappop(stone_heap) # -2
            if first_max != second_max:
                heapq.heappush(stone_heap, (first_max-second_max))

        return -stone_heap[0] if stone_heap else 0

    def lastStoneWeight_1(self, stones):
        stones.sort()
        while(len(stones)>1):
            stone1 = stones.pop()
            stone2 = stones.pop()
            stones.append(stone1-stone2)
            stones.sort()
        return stones[0]
