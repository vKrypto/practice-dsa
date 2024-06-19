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
    
    

def recursive_solution(points):
    
    def rec(day, last_task=None):
        if day < 0:
            return 0
        max_points = float('-inf')
        for task_index, task_point in enumerate(points[day]):
            if task_index != last_task:
                max_points = max(max_points, task_point + rec(day-1, task_index))
        return max_points
    
    return rec(len(points)-1)


def main_2():
    points = [[10,40,70],
              [20,50,80],
              [200,60,80],
              [20,50,20],
              [30,60,90]]
    print(recursive_solution(points))

if __name__ == '__main__':
    main()
    main_2()
    
    
def solve(arr, target):
    
    def rec(i, total):
        if total > target:
            return False
        if total == target:
            return True
        
        if rec(i+1, total+i) or rec(i+1, total):
            return True
        
        return False
    
    
def knapsack(weights, vals, capacity):
    
    def rec(i, total_weight):
        # base-case
        if total_weight > capacity:
            return 0
        if i == len(weights):
            return 0
        
        case_1 = rec(i+1, total_weight+weights[i]) + vals[i]
        case_2 = rec(i+1, total_weight)
        
        return max(case_1, case_2)
