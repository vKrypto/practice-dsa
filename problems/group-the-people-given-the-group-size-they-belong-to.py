# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/
from typing import List
from collections import defaultdict


class Solution:
    # time: o(n), space: o(n)
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group = defaultdict(list)
        res = []

        for index, group_size in enumerate(groupSizes):
            group[group_size].append(index)

            # check if group is full
            if len(group[group_size]) == group_size:
                res.append(group[group_size])
                del group[group_size]

        return res
