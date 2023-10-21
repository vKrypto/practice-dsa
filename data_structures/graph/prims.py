# A Python3 program for Prim's Minimum Spanning Tree (MST) algorithm.
# The program is for adjacency matrix representation of the graph

import sys 


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def minKey(self, dist):

        min = sys.maxsize

        for v in range(self.V):
            if dist[v] < min:
                min = dist[v]
                min_index = v

        return min_index

    def primMST(self):

        dist = [sys.maxsize] * self.V
        parent = [None] * self.V 
        visited = [False] * self.V

        parent[0] = -1 
        dist[0] = 0

        for _ in range(self.V):

            u = self.minKey(dist)

            visited[u] = True

            for v in range(self.V):
                w = self.graph[u][v]
                if w and not visited[v] and dist[v] > w:
                    dist[v] = w
                    parent[v] = u
            dist[u] = sys.maxsize
        self.printMST(parent)


# Driver's code
if __name__ == '__main__':
    g = Graph(5)
    g.graph = [[0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]

    g.primMST()

