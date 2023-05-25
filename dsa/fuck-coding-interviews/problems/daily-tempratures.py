# https://leetcode.com/problems/daily-temperatures/submissions/957261343/

from . import List

class Solution:

    # time: o(n**2), space=O(n)
    def dailyTemperatures_1(self, temperatures: List[int]) -> List[int]:
        temp_indexing = []
        len_temps = len(temperatures)
        res = [None for _ in range(len_temps)]
        temp_stack = []

        for index in range(len_temps-1, -1, -1):
            days = 0
            for i in temp_stack[::-1]:
                days += 1
                if i > temperatures[index]:
                    break
            if temp_stack and not (i > temperatures[index]):
                days = 0

            res[index] = days
            temp_stack.append(temperatures[index])
        
        return res

    # time: o(n), space=O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res