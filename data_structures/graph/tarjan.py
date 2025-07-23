# Python program to find articulation points in an undirected graph

from collections import defaultdict


class TarzanGraph:

    def __init__(self, vertices):
        self.V = vertices 
        self.graph = defaultdict(list) 
        self.Time = 0

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # implementation of SCC, bridges and articulation points.
    def SCC(self):
        self.timer = 0
        disc = [float("Inf")] * (self.V) # discovery timer as per dfs traversal
        low = [float("Inf")] * (self.V) # lowest possible discovery from any path

        stackMember = [False] * (self.V)
        st = []
        bridges = []
        ap = set()
            
        def dfs(node, root_node=False):
            disc[node] = self.timerm ,
            low[node] = self.timer
            self.timer += 1
            
            stackMember[node] = True
            st.append(node)
            children = 0

            for child_node in self.graph[node]:
                if child_node == node:
                    continue
                if disc[child_node] == float("Inf"):
                    dfs(child_node)
                    low[node] = min(low[node], low[child_node])
                    
                    children += 1
                    # case-1 AP for root node
                    if root_node and children > 1:
                        if node not in ap:
                            ap.add(node)
                    # case-2 for ap, but not root node
                    if not root_node and low[child_node] >= disc[node]:
                        if node not in ap:
                            ap.add(node)
                    # for bridges
                    if (low[child_node] > disc[node]):
                        bridges.append((child_node, node))

                elif stackMember[child_node]:
                    low[node] = min(low[node], disc[child_node])

            # head node found, pop the stack and print an SCC
            w = -1 # To store stack extracted vertices
            if low[node] == disc[node]:
                print("scc: >>", end=" ")
                while w != node:
                    w = st.pop()
                    print(w, end=" ")
                    stackMember[w] = False

                print()
                
        for i in range(self.V):
            if disc[i] == float("Inf"):
                dfs(i, root_node=True)
        print("Bridges: ", bridges)
        print("AP: ", ap)


g1 = TarzanGraph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)

print("Strongly connected Components in first graph ")
g1.SCC()

g2 = TarzanGraph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print("Strongly connected Components in first graph ")
g2.SCC()


g1 = TarzanGraph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
print("Strongly connected Components in first graph ")
g1.SCC()

g2 = TarzanGraph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print("\nStrongly connected Components in second graph ")
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
print("\nStrongly connected Components in third graph ")
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
print("\nStrongly connected Components in fourth graph ")
g4.SCC()


g5 = TarzanGraph(5)
g5.addEdge(0, 1)
g5.addEdge(1, 2)
g5.addEdge(2, 3)
g5.addEdge(2, 4)
g5.addEdge(3, 0)
g5.addEdge(4, 2)
print("\nStrongly connected Components in fifth graph ")
g5.SCC()
