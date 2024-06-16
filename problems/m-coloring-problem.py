


class Solution:
    def __init__(self) -> None:
        self.nodes = 4
        # generate a random adjacency list graph
        self.graph = [
            [0, 1, 1, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 1],
            [1, 0, 1, 0]
        ]
    
    def mColoring(self, k: int) -> int:
        # base-case : 1
        if k >= self.nodes:
            return True
        # base-case : 2
        max_connected = 0
        for i in range(self.nodes):
            max_connected = max(max_connected, sum(self.graph[i]))
        if max_connected < k:
            return False
        
        n = self.nodes
        
        colors = [None]*n
        res = []
        
        def rec(node):
            # base-case
            if node == n:
                res.append(colors[::])
                return True
            
            # recursion
            for color in range(k):
                colors[node] = color
                
                is_valid = True
                for child, weight in enumerate(self.graph[node]):
                    if weight == 1 and colors[node] == colors[child]:
                        is_valid = False
                        break
                if is_valid:
                    if rec(node+1):
                        return True
                colors[node] = None
                
            return False
        
        is_valid = rec(0)
        min_colors = float('inf')
        for r in res:
            min_colors = min(min_colors, len(set(r)))
            print("valid way to color: ", r)
        print("min color: ", min_colors)
        
        print(is_valid)
        
        
Solution().mColoring(3)