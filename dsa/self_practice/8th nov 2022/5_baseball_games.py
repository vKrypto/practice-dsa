# https://leetcode.com/problems/baseball-game/description/

from typing import List

# @lc code=start
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
        