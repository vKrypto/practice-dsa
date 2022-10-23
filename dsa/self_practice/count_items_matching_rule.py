# https://leetcode.com/problems/count-items-matching-a-rule/submissions/

class Solution:
    # Runtime: 349 ms, faster than 61.23% of Python3 online submissions for Count Items Matching a Rule.
    # Memory Usage: 20.2 MB, less than 83.91% of Python3 online submissions for Count Items Matching a Rule.
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        map = {
            "type": 0, "color": 1, "name":2
        }
        matched_count = 0
        for item in items:
            if item[map[ruleKey]] == ruleValue:
                matched_count +=1 
        return matched_count