from collections import defaultdict

                            
class DisjointSetGraph:
    
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.parent = [-1] * n
        self.edges = []

    def find(self, node):
        if self.parent[node] < 0:
            return node
        else:
            parent = self.find(self.parent[node])
            self.parent[node] = parent
            return parent
        
    
    def add_edge(self, from_node, to_node):
        edge = (from_node, to_node)
        self.edges.append(edge)
        self.graph[from_node].append(to_node)
        a = self.find(from_node)
        b = self.find(to_node)
        if a == b:
            return            
        #  both belong to the different family
        weight_a = self.parent[a]
        weight_b = self.parent[b]

        # may need to update all member's parent
        if weight_a > weight_b:
            self.parent[a] = weight_a + weight_b
            self.parent[b] = a 
        elif weight_a < weight_b:
            self.parent[b] = weight_a + weight_b
            self.parent[a] = b 
        else:
            self.parent[a] = weight_a + weight_b
            self.parent[b] = a
    
    def remove_edge(self, edge):
        pass
    
    def find_bridges(self):
        bridges = []
        for edge in self.edges:
            self.remove_edge(edge)            
            from_node, to_node = edge
            parent_from = self.find(from_node)
            parent_to = self.find(to_node)
            if parent_from != parent_to:
                bridges.append(edge)
        return bridges



class TarzanGraph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    '''A recursive function that find finds and prints strongly connected
    components using DFS traversal
    u --> The vertex to be visited next
    disc[] --> Stores discovery times of visited vertices
    low[] -- >> earliest visited vertex (the vertex with minimum
                discovery time) that can be reached from subtree
                rooted with current vertex
    st -- >> To store all the connected ancestors (could be part
        of SCC)
    stackMember[] --> bit/index array for faster check whether
                a node is in stack
    '''



    def SCC(self):

        disc = [-1] * (self.V)
        low = [-1] * (self.V)
        stackMember = [False] * (self.V)
        st = []
        
        def dfs(node):
            disc[node] = self.Time
            low[node] = self.Time
            self.Time += 1
            stackMember[node] = True
            st.append(node)

            for child_node in self.graph[node]:
                if disc[child_node] == -1:
                    dfs(child_node)
                    low[node] = min(low[node], low[child_node])

                elif stackMember[child_node]:
                    low[node] = min(low[node], disc[child_node])

            # head node found, pop the stack and print an SCC
            w = -1 # To store stack extracted vertices
            if low[node] == disc[node]:
                while w != node:
                    w = st.pop()
                    print(w, end=" ")
                    stackMember[w] = False

                print()
                
        for i in range(self.V):
            if disc[i] == -1:
                dfs(i)


# Create a graph given in the above diagram
g1 = TarzanGraph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
print("SSC in first graph ")
g1.SCC()

g2 = TarzanGraph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print("\nSSC in second graph ")
g2.SCC()


g3 = TarzanGraph(7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
print("\nSSC in third graph ")
g3.SCC()

g4 = TarzanGraph(11)
g4.addEdge(0, 1)
g4.addEdge(0, 3)
g4.addEdge(1, 2)
g4.addEdge(1, 4)
g4.addEdge(2, 0)
g4.addEdge(2, 6)
g4.addEdge(3, 2)
g4.addEdge(4, 5)
g4.addEdge(4, 6)
g4.addEdge(5, 6)
g4.addEdge(5, 7)
g4.addEdge(5, 8)
g4.addEdge(5, 9)
g4.addEdge(6, 4)
g4.addEdge(7, 9)
g4.addEdge(8, 9)
g4.addEdge(9, 8)
print("\nSSC in fourth graph ")
g4.SCC()


g5 = TarzanGraph(5)
g5.addEdge(0, 1)
g5.addEdge(1, 2)
g5.addEdge(2, 3)
g5.addEdge(2, 4)
g5.addEdge(3, 0)
g5.addEdge(4, 2)
print("\nSSC in fifth graph ")
g5.SCC()
