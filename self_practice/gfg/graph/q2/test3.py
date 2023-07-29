from collections import defaultdict

def dfs(node, graph, visited):
    visited[node] = True
    max_depth = 0

    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            max_depth = max(max_depth, dfs(neighbor, graph, visited) + weight)

    return max_depth

def max_depth_in_weighted_graph(graph, start_node):
    visited = defaultdict(bool)

    # Call DFS from the start_node
    return dfs(start_node, graph, visited)

# Example usage:
graph = defaultdict(list)
graph[1].append((2, 3))
graph[2].append((3, 4))
graph[2].append((4, 2))
graph[4].append((5, 5))

start_node = 1
max_depth = max_depth_in_weighted_graph(graph, start_node)
print("Maximum depth from node", start_node, "is", max_depth)
