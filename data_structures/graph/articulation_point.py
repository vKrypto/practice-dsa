from collections import defaultdict


class Graph1:
    
    def __init__(self) -> None:
        self.graph = defaultdict(set)
        
    # o(v*e*(v+e))
    def method_1_brute(self):
        for node in range(self.n):
            visited = dfs_lookup(ignore_node=node)            
            if len(visited) != self.V:
                return node
    
    # o(v+e)
    def check_for_root_node(self, node):
        # if dfs tree has two children on root node, then it's a articulation point
        dfs(node)
        
    # o(v((v+e)))
    def method_1_brute(self):
        for node in range(self.n):
            self.check_for_root_node(node)

# Python program to find articulation points in an undirected graph


class Graph:

	def __init__(self, vertices):
		self.V = vertices 
		self.graph = defaultdict(list) 
		self.Time = 0

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def APUtil(self, u, visited, ap, parent, low, disc):

		# Count of children in current node
		children = 0

		# Mark the current node as visited and print it
		visited[u]= True

		# Initialize discovery time and low value
		disc[u] = self.Time
		low[u] = self.Time
		self.Time += 1

		# Recur for all the vertices adjacent to this vertex
		for v in self.graph[u]:
			# If v is not visited yet, then make it a child of u
			# in DFS tree and recur for it
			if visited[v] == False :
				parent[v] = u
				children += 1
				self.APUtil(v, visited, ap, parent, low, disc)

				# Check if the subtree rooted with v has a connection to
				# one of the ancestors of u
				low[u] = min(low[u], low[v])

				# u is an articulation point in following cases
				# (1) u is root of DFS tree and has two or more children.
				if parent[u] == -1 and children > 1:
					ap[u] = True

				#(2) If u is not root and low value of one of its child is more
				# than discovery value of u.
				if parent[u] != -1 and low[v] >= disc[u]:
					ap[u] = True
					
				# Update low value of u for parent function calls
			elif v != parent[u]:
				low[u] = min(low[u], disc[v])


	# The function to do DFS traversal. It uses recursive APUtil()
	def AP(self):

		# Mark all the vertices as not visited
		# and Initialize parent and visited,
		# and ap(articulation point) arrays
		visited = [False] * (self.V)
		disc = [float("Inf")] * (self.V)
		low = [float("Inf")] * (self.V)
		parent = [-1] * (self.V)
		ap = [False] * (self.V) # To store articulation points

		# Call the recursive helper function
		# to find articulation points
		# in DFS tree rooted with vertex 'i'
		for i in range(self.V):
			if visited[i] == False:
				self.APUtil(i, visited, ap, parent, low, disc)

		for index, value in enumerate (ap):
			if value == True: print (index,end=" ")

g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)

print ("\nArticulation points in first graph ")
g1.AP()

g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print ("\nArticulation points in second graph ")
g2.AP()

