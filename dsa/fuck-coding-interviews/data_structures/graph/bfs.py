
class Graph:
    def __init__(self, node_count) -> None:
        self.node_count = node_count
        self.graph =[[]] 
        
    def bfs(self, source=0):
        visited = set()
        path = []
        queue = [source]
        while queue:
            cur_node = queue.pop(0)
            if cur_node not in visited:
                path.append(cur_node)
                visited.add(cur_node)
                for neighbor_node, neighbor_node_dist  in enumerate(self.graph[cur_node]):
                    if neighbor_node_dist == 0:
                        continue
                    if neighbor_node not in visited:
                        queue.append(neighbor_node)
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

    g.bfs()

