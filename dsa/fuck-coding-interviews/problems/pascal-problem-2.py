# https://leetcode.com/problems/pascals-triangle-ii/
from typing import List


class Solution:
    
    # space compexity: o(1)
    def get_factorial(self, n):
        if self.rowIndex == n and self.factors.get(n):
            return self.factors[n]
        else:
            # initial cache for factorial
            factor = 1
            for i in range(1, n+1):
                factor *= (i+1)
            return factor

    # space compexity: o(n)
    def get_cached_factorial(self, n):
        if self.rowIndex == n and self.factors.get(n):
            return self.factors[n]
        else:
            # initial cache for factorial
            self.factors[0] = 1
            for i in range(1, n+1):
                self.factors[i] = self.factors[i-1] * (i)
            return self.factors[n]

    """
    time complexity: O(n/2)
    spaceComplexity: o(n) 
    Runtime: 34 ms, faster than 90.83% of Python3 online submissions for Pascal's Triangle II.
    Memory Usage: 13.8 MB, less than 64.30% of Python3 online submissions for Pascal's Triangle II.
    """
    def getRow_5(self, rowIndex: int) -> List[int]:
        """
        nC0, nC1, nC2, .... nCn { n+1 items [0, n]} where  ncr= n! / ( r! * (n-r)!)
        """
        self.rowIndex = rowIndex
        self.factors = {}
        self.fact_n = self.get_cached_factorial(rowIndex)
        

        res = []
        for i in range((rowIndex)//2 +1):
            denomi = self.get_cached_factorial(i) * self.get_cached_factorial(rowIndex-i)
            res.append(int(self.fact_n/denomi))
        
        if rowIndex%2 != 0:
            return res + res[::-1]
        else:
            return res + res[::-1][1:]
            
        
            

    """
    time complexity: O(n*2/2)
    spaceComplexity: O(1)
    Runtime: 34 ms, faster than 90.83% of Python3 online submissions for Pascal's Triangle II.
    Memory Usage: 13.8 MB, less than 96.87% of Python3 online submissions for Pascal's Triangle II.
    """
    def getRow_4(self, rowIndex: int) -> List[int]:
        """
        nC0, nC1, nC2, .... nCn { n+1 items [0, n]} where  ncr= n! / ( r! * (n-r)!)
        """
        self.rowIndex = rowIndex
        self.fact_n = self.get_factorial(rowIndex)
        

        res = []
        for i in range((rowIndex)//2 +1):
            denomi = self.get_factorial(i) * self.get_factorial(rowIndex-i)
            res.append(int(self.fact_n/denomi))
        
        if rowIndex%2 != 0:
            return res + res[::-1]
        else:
            return res + res[::-1][1:]
            
        
    
    def getRow_3(self, rowIndex: int) -> List[int]:
        """
        binary theorom but unoptimized.
        """
        res = []
        def facto(n):
            fact = 1
            for i in range(n):
                fact *= (i+1)
            return fact
        
        fact_n = facto(rowIndex)
        for i in range(rowIndex+1):
            res.append(int(fact_n/(facto(i) * facto(rowIndex-i))))
                             
        return res

    """
    time complexity : O(n*2)
    space complexity: o(n* (n+1)/2) >> O(n*2)
    Runtime: 43 ms, faster than 73.60% of Python3 online submissions for Pascal's Triangle II.
    Memory Usage: 14 MB, less than 16.78% of Python3 online submissions for Pascal's Triangle II.
    """
    def getRow_1(self, rowIndex: int) -> List[int]:
        """
        iterative solution. ( compute whole tree.)
        """
        lst=[]
        for i in range(0,rowIndex+1):            
            temp=[]
            for j in range(0,i+1):
                if  j==0 or i==j:
                    temp.append(1)
                else:
                    temp.append(lst[i-1][j]+lst[i-1][j-1])
            lst.append(temp)
        
        return lst[rowIndex]
    
    """
    time complexity : O(n*2)
    space complexity: o(n)
    Runtime: 57 ms, faster than 41.06% of Python3 online submissions for Pascal's Triangle II.
    Memory Usage: 13.8 MB, less than 64.30% of Python3 online submissions for Pascal's Triangle II.    """
    def getRow_2(self, rowIndex: int) -> List[int]:
        """
        iterative solution. ( compute whole tree.)
        """
        lst=[]
        for i in range(0,rowIndex+1):            
            temp=[]
            for j in range(0,i+1):
                if  j==0 or i==j:
                    temp.append(1)
                else:
                    temp.append(lst[i-1][j]+lst[i-1][j-1])
            lst.append(temp)
        
        return lst[rowIndex]
        