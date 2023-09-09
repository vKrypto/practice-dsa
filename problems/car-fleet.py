# https://leetcode.com/problems/car-fleet/

from typing import List, int

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        step 1: create a list with sorted by position decreasing
        position_speed: [(10, 2), (8, 4), (5, 1), (3, 3), (0, 1)] #
        """
        position_speed = []
        for pos, sp in zip(position, speed):
            position_speed.append((pos, sp))
        position_speed.sort(reverse=True)

        """
        step 2:
        """
        stack = []
        for (x, v) in position_speed:
            time_to_finish_target = (target-x)/v
            if not stack or stack[-1] < time_to_finish_target:
                stack.append(time_to_finish_target)            

        return len(stack)

    def carFleet_2(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        step 1: create a list with sorted by position decreasing
        position_speed: [(10, 2), (8, 4), (5, 1), (3, 3), (0, 1)] #
        """
        position_speed = []
        for pos, sp in zip(position, speed):
            position_speed.append((pos, sp))
        position_speed.sort(reverse=True)

        """
        step 2: 
        """
        fleet_count = 0
        last_fleet_time = None
        for (x, v) in position_speed:
            time_to_finish_target = (target-x)/v
            if last_fleet_time is None or last_fleet_time < time_to_finish_target:
                last_fleet_time = time_to_finish_target      
                fleet_count += 1
        return fleet_count