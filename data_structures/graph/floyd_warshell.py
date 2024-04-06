from collections import defaultdict
import sys

class Graph:
    def __init__(self, node_count) -> None:
        self.node_count = node_count
        self.graph = defaultdict(list)

    def floyd(self):
        for k in range(self.node_count):
            for i in range(self.node_count):
                for j in range(self.node_count):
                    self.graph[i][j] = min(
                        self.graph[i][j],
                        self.graph[i][k]+ self.graph[k][j])
    
        return self.graph

# Driver's code
if __name__ == '__main__':
    g = Graph(9)
    mx = sys.maxsize
    g.graph = [[0, 4,mx,mx,mx,mx,mx, 8, mx],
               [4,0, 8,mx,mx,mx,mx, 11, mx],
               [mx, 8,0, 7,mx, 4,mx,mx, 2],
               [mx,mx, 7,0, 9, 14,mx,mx, mx],
               [mx,mx,mx, 9,0, 10,mx,mx, mx],
               [mx,mx, 4, 14, 10,0, 2,mx, mx],
               [mx,mx,mx,mx,mx, 2,0, 1, 6],
               [8, 11,mx,mx,mx,mx, 1,0, 7],
               [mx,mx, 2,mx,mx,mx, 6, 7, 0]
               ]

    print(g.floyd())

import heapq
# prims algo
graph = {}

src = 0
visited = set()
queue = [0, 0, -1]
mst = []

while queue:
    weight, from_node, to_node = heapq.heappop(queue)
    if from_node in visited: continue
    if from_node != -1:
        mst.append([weight, from_node, to_node])
    visited.add(from_node)
    for child, child_weight in graph[from_node]:
        if child not in visited:
            heapq.heappush(queue, [child_weight, from_node, child])
    
