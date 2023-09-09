# https://leetcode.com/problems/daily-temperatures/submissions/957261343/

from typinf import List

class Solution:

    # time: o(n**2)
    def dailyTemperatures_1(self, temperatures: List[int]) -> List[int]:
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

    
    def dailyTemperatures_2(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = [] # [( temp , index)]
        
        index = len(temperatures)
        while index > 0:
            index -= 1
            temp = temperatures[index]

            # make sure last item in stack must be greater than cur_item
            while stack and stack[-1][0] <= temp:
                stack.pop()
            
            # res[index] = cur_index - last_item_index in stack
            if stack:
                res[index] = stack[-1][1] - index
            
            # append entry in stack
            stack.append((temp, index))
        return res
    

    # time: o(n), space=O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackInd, _ = stack.pop()
                res[stackInd] = index - stackInd
            stack.append((index, temp))
        return res
    
