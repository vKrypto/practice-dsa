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



# space: o(2(n*(k+1))), time: o(n*(k*(k-1)))
def ninjaTraining(days, points):
    task_count = len(points[0]) + 1
    prev = [0]*task_count

    for day in range(days):
        cur_day = [0]*task_count
        for last in range(task_count):
            max_point = 0
            # find max point task while ignoring last task
            for task in range(task_count-1):
                if task != last:
                    max_point = max(max_point, points[day][task] + prev[task])
            cur_day[last] = max_point
        prev = cur_day
    return prev[3]

def main():
    points = [[10,40,70],
              [20,50,80],
              [200,60,80],
              [20,50,20],
              [30,60,90]]
    n = len(points)
    print(ninjaTraining(n, points))

if __name__ == '__main__':
    main()