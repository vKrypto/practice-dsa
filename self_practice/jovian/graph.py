from collections import defaultdict
import queue
edges = [
    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (1, 0)
]

class BiDirectionalGraph:

    # nodes must be repesent by 0-n, adjency list
    def __init__(self, edges, node_count) -> None:
        self.data = [[] for _ in range(node_count)]
        for node_1, node_2 in edges:
            self.data[node_1].append(node_2)
            self.data[node_2].append(node_1)
        
    # nodes must be repesent by 0-n : matrix version: adjency matrix
    def __init__(self, edges, node_count) -> None:
        self.data = [[0]*node_count]*node_count
        for node_1, node_2 in edges:
            self.data[node_1][node_2] = 1
            self.data[node_2][node_1] = 1
        
    # node names must be hashable: adjency hash
    def __init__(self, edges) -> None:
        self.data = defaultdict(set)
        for node_1, node_2 in edges:
            self.data[node_1].add(node_2)
            self.data[node_2].add(node_1)
        
        
    def bfs(self, source):
        visited = defaultdict(bool)
        path = [source]
        i = 0
        while i < len(path):
            current_node = path[i]
            for node in self.data[current_node]:
                if not visited[node]:
                    path.append(node)
                    visited[node] = True
            i += 1
        return path

    def bfs(self, source):
        
        visited = defaultdict(bool) # {node: True}
        parent_map = defaultdict() # {node: parent_node}
        distance_map = defaultdict(int) # {node: distance from source node}
        path = [source] #traverse path [0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9]


        def _visit(node, distance, parent_node):
            visited[node] = True
            parent_map[node] = parent_node
            distance_map[node] = distance
            path.append(node)

        level_queue = queue([source])
        distance = 0
        while level_queue:
            distance += 1
            cur_node = level_queue.popleft()
            for node in self.data[cur_node]:
                if not visited[node]:
                    level_queue.append(node)
                    _visit(node, distance, cur_node)

        return path
