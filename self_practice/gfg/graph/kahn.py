from collections import defaultdict

class Graph:
    def __init__(self, node_count) -> None:
        self.node_count = node_count
        self.graph = defaultdict(list)

    def topological_sort(self, source=0):
        # step : 1
        # in_bound = [] loop in nodes and calculate in bound edges
        in_bound = []
        
        # step 2:        
        # queue = nodes having in_bound == 0
        queue = [i for (i,w) in enumerate(in_bound) if w==0]
        # step 3:
        visited = {}
        res = []
        while queue:
            node = queue.pop(0)
            visited.add(node)
            res.append(node)
            for child in node.neighbors:
                in_bound[child] -= 1
                if in_bound[child] == 0:
                    queue.append(child)
        
        return res
    
    

# Driver's code
if __name__ == '__main__':
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]

    g.dfs_iterative()
    g.dfs_recursive()

