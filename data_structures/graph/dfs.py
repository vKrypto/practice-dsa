from collections import defaultdict

class Graph:
    def __init__(self, node_count) -> None:
        self.node_count = node_count
        self.graph = defaultdict(list)
        
    def dfs_iterative(self, source=0):
        visited = set()
        path = []
        stack = [source]
        while stack:
            cur_node = stack.pop()
            
            if cur_node in visited:
                continue
            
            path.append(cur_node)
            visited.add(cur_node)
            for neighbor_node, neighbor_node_dist  in enumerate(self.graph[cur_node]):
                if neighbor_node_dist != 0 and neighbor_node not in visited:
                    stack.append(neighbor_node)
        print(path)


    def dfs_recursive(self, source=0):
        visited = set() 
        path = []
        def dfs(node=source):
            if node in visited:
                return
            
            visited.add(node)
            path.append(node)    
            for neighbor_node, neighbor_node_weight in enumerate(self.graph[node]):
                if neighbor_node_weight !=0 and neighbor_node not in visited:
                    dfs(neighbor_node)
        dfs()
        print(path)
    
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

