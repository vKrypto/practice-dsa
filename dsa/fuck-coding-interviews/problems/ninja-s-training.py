# https://www.codingninjas.com/studio/problems/ninja-s-training_3621003

from typing import List
from collections import defaultdict

  
def ninjaTraining_recursive(n: int, points: List[List[int]]) -> int:

    memo = defaultdict(list)
    # Write your code here.
    def rec(index, last_task=None):
        if index < 0:
            return 0
        if (index, last_task) in memo:
            return memo[(index, last_task)]

        max_points = 0
        for task_index, task_point in enumerate(points[index]):
            if task_index != last_task:
                max_points = max(max_points, task_point + rec(index-1, task_index))
        
        memo[(index, last_task)] = max_points
        return max_points

    return rec(len(points)-1)


def ninjaTraining(n: int, points: List[List[int]]) -> int:

    memo = [[0]* (len(points[0]) + 1) for _ in len(points)]
    
    # for day-0, memo[0]
    
    # Write your code here.
    def rec(index, last_task=None):
        if index < 0:
            return 0
        if (index, last_task) in memo:
            return memo[(index, last_task)]

        max_points = 0
        for task_index, task_point in enumerate(points[index]):
            if task_index != last_task:
                max_points = max(max_points, task_point + rec(index-1, task_index))
        
        memo[(index, last_task)] = max_points
        return max_points

    return rec(len(points)-1)