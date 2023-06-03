# https://leetcode.com/problems/baseball-game/description/

from typing import List


class Solution:
    """
    Runtime: 46 ms, faster than 89.95% of Python3 online submissions for Baseball Game.
    Memory Usage: 13.9 MB, less than 99.70% of Python3 online submissions for Baseball Game.
    """
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for op in operations:
            if op == "+":
                records.append(records[-1] + records[-2])
            elif op == "D":
                records.append(records[-1] * 2)
            elif op == 'C':
                records.pop()
            else:
                records.append(int(op))
        return sum(records)
        
    def calPoints_2(self, operations: List[str]):
        """
        time: o(1)
        space: o(1)
        #pattern: 
        we can do the same thing with following pointers only.
        last_second, last = 0, 0
        total_sum = 0
        won't work...
        """ 
        # last_second, last = 0, 0
        # total_sum = 0
        # for op in operations:
        #     if op == "+":
        #         last_second, last = last, last_second + last
        #         total_sum += last
        #     elif op == "D":
        #         last_second, last = last, last*2
        #         total_sum += last
        #     elif op == 'C':
        #         total_sum -= last
        #         last_second, last = 0, last_second
        #     else:
        #         last_second, last = last, int(op)
        #         total_sum = int(op)
        # return total_sum
    