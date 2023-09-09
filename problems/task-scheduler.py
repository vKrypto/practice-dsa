# coding: utf-8
"""
https://leetcode.com/problems/task-scheduler/
"""
from collections import Counter, deque
from typing import List
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        recorded_tasks = []
        queue = []
        for task, count in Counter(tasks).items():
            # heapq is min heap, so make count negative.
            heapq.heappush(queue, (-count, task))

        # We should schedule the most frequent tasks as frequently as possible.
        while queue:
            put_backs = []
            for _ in range(n + 1):
                if queue:
                    # Pop the current most frequent task.
                    count, task = heapq.heappop(queue)
                    # We don't need to check whether the popped task is in recorded_tasks[-n:] or not.
                    recorded_tasks.append(task)
                    count += 1
                    if count < 0:
                        put_backs.append((count, task))
                else:
                    if put_backs:
                        recorded_tasks.append('idle')
                    else:
                        break

            for task_data in put_backs:
                heapq.heappush(queue, task_data)

        # print(recorded_tasks)

        return len(recorded_tasks)



class Solution2:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count_heap = [-i for i in  Counter(tasks).values()] # o(n), o(n)
        heapq.heapify(task_count_heap)

        time = 0
        waiting_queue = deque()  #  [-cnt, idleTime]
        while task_count_heap or waiting_queue:
            time += 1
            if task_count_heap:
                # pick most count task
                cnt = 1 + heapq.heappop(task_count_heap)
                # if task not finished, send to waiting_queue
                if cnt:
                    waiting_queue.append([cnt, time + n])
            # check for waiting queue items
            if waiting_queue and waiting_queue[0][1] == time:
                heapq.heappush(task_count_heap, waiting_queue.popleft()[0])
        return time

    def leastInterval_optimized(self, tasks: List[str], n: int) -> int:
        task_count_heap = [-i for i in  Counter(tasks).values()] # o(n), o(n)
        heapq.heapify(task_count_heap)

        time = 0
        waiting_queue = deque()  #  [-cnt, idleTime]
        while task_count_heap or waiting_queue:
            time += 1
            if not task_count_heap:
                # if task_count_heap does not exist, jump to waiting_queue first task time_stamp
                time = waiting_queue[0][1]
            else:
                # pick most count task
                cnt = 1 + heapq.heappop(task_count_heap)
                # if task not finished, send to waiting_queue
                if cnt:
                    waiting_queue.append([cnt, time + n])
            # check for waiting queue items
            if waiting_queue and waiting_queue[0][1] == time:
                heapq.heappush(task_count_heap, waiting_queue.popleft()[0])
        return time