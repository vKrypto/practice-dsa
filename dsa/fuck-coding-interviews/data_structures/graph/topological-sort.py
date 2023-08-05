# A Python program to print topological sorting of a graph
# using indegrees

from collections import defaultdict

class Graph:
	def __init__(self, vertices):
		self.graph = defaultdict(list) 
		self.V = vertices 

	def addEdge(self, u, v):
		self.graph[u].append(v)


	def topologicalSort(self):
		
		in_degree = [0]*(self.V)
		
		# step 1: calculate in_degree for each node.
		for i in self.graph:
			for j in self.graph[i]:
				in_degree[j] += 1
		print("step 1: in_degree: ", in_degree)

		# step 2: create a queue of all nodes having in_degree == 0 as starting case.
		queue = []
		for i in range(self.V):
			if in_degree[i] == 0:
				queue.append(i)
		print("step 2: starting queue :", queue)
		cnt = 0
		top_order = []
        
        # pop from left in queue and while popping decrement in_degree all adjacent nodes by 1.
        # and also add them into queue if in_degree is zero
		while queue:

			u = queue.pop(0)
			top_order.append(u)

			for i in self.graph[u]:
				in_degree[i] -= 1
				if in_degree[i] == 0:
					queue.append(i)

			cnt += 1

		if cnt != self.V:
			print ("There exists a cycle in the graph")
		else :
			print (top_order)


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print ("Following is a Topological Sort of the given graph")
g.topologicalSort()

