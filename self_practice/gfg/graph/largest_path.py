# find largest path in graph from a node to others
from collections import defaultdict
maxsize = -10**9

class Graph:
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.graph = defaultdict(list)
        self.top_sort_stack = []
    
    def _topologicalSortUtil(self):
        visited = [False]*self.vertices
        
        def dfs(v):
            visited[v] = True
            for [i,_] in self.graph[v]:
                if (not visited[i]):
                    dfs(i)
            self.top_sort_stack.append(v)

        # loop through all vertices
        for i in range(self.vertices):
            if not visited[i]:
                dfs(i)

    def iterative_longestPath(self, source=0):
        dist = [maxsize for _ in range(self.vertices)]

        self._topologicalSortUtil()

        dist[source] = 0
        # Process vertices in topological order
        while len(self.top_sort_stack) > 0:
            node = self.top_sort_stack.pop()
            # relaxation of distance
            if (dist[node] != maxsize):
                for [child_node, weight] in self.graph[node]:
                    if (dist[child_node] < dist[node] + weight):
                        dist[child_node] = dist[node] + weight

        for i in range(self.vertices):
            print("INF ",end="") if (dist[i] == maxsize) else print(dist[i],end=" ")
        print("")


    def recursive_longestPath(self, source=0):
        def relax(node):
            for [child_node, weight] in self.graph[node]:
                if dist[child_node] < dist[node] + weight:
                    dist[child_node] = dist[node] + weight
                    relax(child_node)
                    
        dist = [maxsize for _ in range(self.vertices)]
        dist[source] = 0
        self._topologicalSortUtil()
        
        while len(self.top_sort_stack) > 0:
            node = self.top_sort_stack.pop()
            if dist[node] != maxsize:
                relax(node)

        for i in range(self.vertices):
            print("INF ",end="") if (dist[i] == maxsize) else print(dist[i],end=" ")
        print("")


# Driver code
if __name__ == '__main__':
    
    g = Graph(7)
    adj = g.graph
    adj[0].append([1, 5])
    adj[0].append([2, 3])
    adj[1].append([3, 6])
    adj[1].append([2, 2])
    adj[2].append([4, 4])
    adj[2].append([5, 2])
    adj[2].append([3, 7])
    adj[3].append([5, 1])
    adj[3].append([4, -1])
    adj[4].append([5, -2])

    s = 1
    print("Following are longest distances from source vertex ",s)
    g.iterative_longestPath(s)
    g.recursive_longestPath(s)
