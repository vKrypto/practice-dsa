
# shortest_path_to_all_node(from_node) or shortest_distance_to_all_node(from_node)


class Graph:

	def __init__(self, vertices):
		self.V = vertices 
		self.graph = []

	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])

	def printArr(self, dist):
		print("Vertex Distance from Source")
		for i in range(self.V):
			print("{0}\t\t{1}".format(i, dist[i]))

	# also detects negative weight cycle
	def BellmanFord(self, src):

		dist = [float("Inf")] * self.V
		dist[src] = 0

		# Step 2: Relax all edges |V| - 1 times. A simple shortest
		for _ in range(self.V - 1):
			for u, v, w in self.graph:
				dist[v] = min(dist[v], dist[u] + w)

		# Step 3: do one more time to check negative weight cycles cycle
		for u, v, w in self.graph:
			if dist[u] != float("Inf") and dist[u] + w < dist[v]:
				print("Graph contains negative weight cycle")
				return

		# print all distance
		self.printArr(dist)


# Driver's code
if __name__ == '__main__':
	g = Graph(5)
	g.addEdge(0, 1, -1)
	g.addEdge(0, 2, 4)
	g.addEdge(1, 2, 3)
	g.addEdge(1, 3, 2)

	g.addEdge(3, 2, 5)
	g.addEdge(3, 1, 1)
	g.addEdge(4, 3, -3)

	# function call
	g.BellmanFord(0)
