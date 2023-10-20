class Solution:
    def mostVisited(self, n: int, rounds):
        d = {i: 0 for i in range(n+1)}

        start = 0
        for end in rounds:
            while start != end:
                start += 1
                start = start%n
                d[start] += 1
        # print(d) # {1: 2, 2: 2, 3: 1, 0: 1}, {sector: visit_count}
        print(d.keys())
        
    
Solution().mostVisited(4, [1,3,1,2])