# A Python3 program for Prim's Minimum Spanning Tree (MST) algorithm.
# The program is for adjacency matrix representation of the graph


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]
    
    def kosaraju(self):
        cycle_set = set()
        
        def dfs(node, parent=set()):
            parent.add(node.val)
            for neighbor in self.graph[node]:
                if neighbor in parent:
                    cycle_set.add(parent)
                    parent = set()
                dfs(neighbor, parent)
        

# Driver's code
if __name__ == '__main__':
    g = Graph(5)
    g.graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]

    g.primMST()

