# https://leetcode.com/problems/find-median-from-data-stream/description/
import heapq


class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []

    def addNum(self, num: int) -> None:
        if self.right_heap and num > self.right_heap[0]:
            heapq.heappush(self.right_heap, num)
        else:
            heapq.heappush(self.left_heap, -num)

        # make sure abs(len(left)- len(right)) < 1
        if len(self.left_heap) > len(self.right_heap) + 1:
            num = heapq.heappop(self.left_heap)
            heapq.heappush(self.right_heap, -num)
        elif len(self.right_heap) > len(self.left_heap) + 1:
            num = heapq.heappop(self.right_heap)
            heapq.heappush(self.left_heap, -num)

    def findMedian(self) -> float:
        if len(self.left_heap) > len(self.right_heap):
            return -self.left_heap[0]
        elif len(self.left_heap) < len(self.right_heap):
            return self.right_heap[0]
        else:
            return (-self.left_heap[0] + self.right_heap[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()