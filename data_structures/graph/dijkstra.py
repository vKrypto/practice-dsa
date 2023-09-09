
# shortest_path(from_node, to_node) or shortest_distance(from_node, to_node)
import sys


class Graph:
    def __init__(self, node_count) -> None:
        self.node_count = node_count
        self.graph =[[]] 
        
    @staticmethod
    def min_dist_non_visited_node(queue, visited):
        min_node_weight, min_index = sys.maxsize, -1
        for q_index, (node_weight, node) in enumerate(queue):
            if node not in visited and node_weight <  min_node_weight:
                min_node_weight = node_weight
                min_index = q_index
        return min_index
    
    def display_result(self, source, distance):
        print("node", " "*7, f"Min Distance From node {source}")
        for node_index, node_distance in enumerate(distance):
            print(node_index, " "*10, node_distance)
                
        
    def dij(self, source=0):
        distance = [sys.maxsize for i in range(self.node_count)]
        visited = set()
        
        queue = [(0, source)]
        distance[source] = 0
        while queue:
            min_index = self.min_dist_non_visited_node(queue, visited)
            cur_dist, cur_node = queue.pop(min_index)
            visited.add(cur_node)
            for neighbor_node, neighbor_node_dist  in enumerate(self.graph[cur_node]):
                if neighbor_node_dist == 0:
                    continue
                total_distance = cur_dist + neighbor_node_dist
                if total_distance <= distance[neighbor_node]:
                    distance[neighbor_node] = total_distance
                    if neighbor_node not in visited:
                        queue.append((total_distance, neighbor_node))
        self.display_result(source, distance)

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

    g.dij()

