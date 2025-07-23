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
            node = stack.pop()
            
            if node in visited:
                continue
            path.append(node)
            visited.add(node)
            for neighbor_node, neighbor_node_dist  in enumerate(self.graph[node]):
                if neighbor_node_dist != 0 and neighbor_node not in visited:
                    stack.append(neighbor_node)
        print(path)


    def dfs_recursive(self, source=0):
        visited = set() 
        path = []
        def dfs(node=source):
            if node in visited:
                return
            path.append(node)
            visited.add(node)
            for neighbor_node, neighbor_node_dist  in enumerate(self.graph[node]):
                if neighbor_node_dist != 0 and neighbor_node not in visited:
                    dfs(neighbor_node)
        dfs()
        print(path)
    




class Graph2:
    
    def __init__(self, node_count) -> None:
        self.node_count = node_count
        self.graph = defaultdict(list)
    
    def dfs_recursive(self, source):
        visited = [False] * self.node_count
        path = []
        stack = [source]
        while stack:
            node = stack.pop()
            if visited[node]:
                return
            visited[node] = True
            path.append(node)
            for child_node, child_node_weight in enumerate(self.graph[node]):
                if not visited[child_node] and child_node_weight != 0:
                    stack.append(child_node)
                        
        print(path)
        

# Driver's code

""""

Graph (Undirected Weighted):

     (0)--<4>--(1)--<8>-----(2)
      |               |      |
     <8>            <2>     <7>
      |               |      |
     (7)--<11>--(1)--<8>----(8)
      |               |      |
     <1>            <6>     <7>
      |               |      |
     (6)--<2>--(5)--<10>----(4)
           \    |    /
           <4> <14> <9>
            \   |   /
             \  |  /
               (3)

"""
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