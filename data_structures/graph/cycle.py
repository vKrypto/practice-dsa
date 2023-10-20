

class Graph:
    def __init__(self, node_count) -> None:
        self.node_count = node_count
        self.graph =[[]] 
        

    def has_cycle(self):
        # do dfs check with last_parent and make sure, no children are visited before
        visited = [False] * self.node_count
        
        def dfs(node=0, parent=None):
            visited[node] = True
            for child, weight in enumerate(self.graph[node]):
                if weight:
                    if not visited[child]:
                        visited[child] = True
                        dfs(child, parent=node)
                    elif child != parent:
                        return True
            return False
        
        return dfs()
                            

                
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

    print(g.has_cycle())

