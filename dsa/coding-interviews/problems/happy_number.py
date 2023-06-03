# https://leetcode.com/problems/happy-number/description/

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
    
    def get_square_sum(self):
        return sum([int(i)**2 for i in str(self.val)])

    def get_next(self):
        self.next= ListNode(self.get_square_sum())
        return self.next



class Solution:
    """
    404/404 cases passed (82 ms)
    Your runtime beats 7.79 % of python3 submissions
    Your memory usage beats 61.24 % of python3 submissions (13.8 MB)
    """
    # using: List Cycle Detection Algo( better space complexity)
    def isHappyListunOptimized(self, n: int) -> bool:
        results = []
        while True:
            n = self.get_square_sum(n)
            if n == 1:
                return True
            if n in results:
                return False
            results.append(n)

    def get_square_sum(self, n):
        return sum([int(i)**2 for i in str(n)])

    """
    404/404 cases passed (85 ms)
    Your runtime beats 5.7 % of python3 submissions
    Your memory usage beats 14.71 % of python3 submissions (14 MB)
    """
    # using: LinkedList Cycle Detection Algo( better time complexity)
    def isHappyLinkedList(self, n: int) -> bool:
        head = ListNode(n)
        slow = head
        fast = slow.get_next()        
        while slow.val != fast.val:
            fast = fast.get_next().get_next()
            slow = slow.get_next()
            if slow.val == 1 or fast.val ==1:
                return True
        return slow.val == 1 or fast.val ==1

    """
    404/404 cases passed (48 ms)
    Your runtime beats 75.26 % of python3 submissions
    Your memory usage beats 61.24 % of python3 submissions (13.8 MB)
    """
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.get_square_sum(n)      
        while slow != fast:
            fast = self.get_square_sum(self.get_square_sum(fast))
            slow = self.get_square_sum(slow)
            if slow == 1 or fast ==1:
                return True
        return slow == 1 or fast ==1
        

        
# @lc code=end

