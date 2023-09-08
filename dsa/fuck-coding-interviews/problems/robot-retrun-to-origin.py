# https://leetcode.com/problems/robot-return-to-origin/description/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c_map = {
            "L": -1, "R" : 1,
            "U": 1, "D": -1
        }
        i = j = 0
        for move in moves:
            if move in ["L", "R"]:
                i += c_map[move]
            else:
                j += c_map[move]
        
        return i == j== 0