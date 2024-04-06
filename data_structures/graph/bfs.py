
class Graph:
    def __init__(self, node_count) -> None:
        self.node_count = node_count
        self.graph =[[]] 
        
    #  iterative bfs
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

    # recursive solution
    def bfs_recursive(self, source=0):
        visited = set()
        path = []
        levels = [[source]]
        
        def rec(cur_level, level=0):
            next_level = []
            while cur_level:
                cur_node = cur_level.pop(0)
                if cur_node in visited:
                    continue
                visited.add(cur_node)
                path.append(cur_node)
                for neighbor_node, neighbor_node_dist  in enumerate(self.graph[cur_node]):
                    if neighbor_node_dist == 0:
                        continue
                    if neighbor_node not in visited:
                        next_level.append(neighbor_node)
            if next_level:
                levels.append(next_level.copy())
                rec(next_level, level+1)
        
        rec([source])
        print(path)
        self.__print_recursion_tree(levels)
    
    def __print_recursion_tree(self, levels):
        print("-----level wise traversal-----")
        for i, level in enumerate(levels):
            print(f"level: {i}", level)            

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
    print("iterative bfs")
    g.bfs()
    print("recursive bfs")
    g.bfs_recursive()

