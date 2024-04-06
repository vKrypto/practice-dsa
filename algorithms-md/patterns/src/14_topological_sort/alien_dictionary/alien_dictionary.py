from collections import deque, defaultdict

# Time complexity 
# In step ‘d’, each task can become a source only once 
# and each edge (a rule) will be accessed and removed once. 
# Therefore, the time complexity of the above algorithm will be O(V+E), 
# where ‘V’ is the total number of different characters 
# and ‘E’ is the total number of the rules in the alien language. 
# Since, at most, each pair of words can give us one rule, 
# therefore, we can conclude that the upper bound for the rules is O(N), 
# where ‘N’ is the number of words in the input. 
# So, we can say that the time complexity of our algorithm is O(V+N).

# Space complexity 
# The space complexity will be O(V+N), 
# since we are storing all of the rules for each character in an adjacency list.

def find_order(words):
    if len(words) == 0:
        return ""
    
    # initialize graph
    in_degrees = {}
    graph = {}
    for word in words:
        for char in word:
            in_degrees[char] = 0
            graph[char] = []
    
    # build graph
    for i in range(len(words) - 1):
        word_1, word_2 = words[i], words[i+1]
        for j in range(min(len(word_1), len(word_2))):
            parent, child = word_1[j], word_2[j]
            if parent != child:
                graph[parent].append(child)
                in_degrees[child] += 1
                break
                
    # find sources
    sources = deque()
    for vertex in in_degrees:
        if in_degrees[vertex] == 0:
            sources.append(vertex) 
             
    # reduce in degrees and update sources
    sorted_order = []
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for adj_vertex in graph[vertex]:
            in_degrees[adj_vertex] -= 1
            if in_degrees[adj_vertex] == 0:
                sources.append(adj_vertex)
    
    if len(sorted_order) != len(in_degrees):
        return ""
    
    return ''.join(sorted_order)



class Solution:
    
    @classmethod
    def alien_order(self, words):
        # step -1: build graph
        graph = defaultdict(set)
        first_word = words[0]
        for next_word in words[1:]:
            for i in range(min(len(first_word), len(next_word))):
                if first_word[i] != next_word[i]:
                    graph[first_word[i]].add(next_word[i])
                    break
            first_word = next_word
        
        # find in-degree
        in_degrees = defaultdict(int)
        for node, child_nodes in graph.items():
            in_degrees[node] += 0
            for child_node in child_nodes:
                in_degrees[child_node] += 1
        # no deps nodes
        stack = []
        zero_in_degree = [node for node in in_degrees if in_degrees[node] == 0]
        while zero_in_degree:
            node = zero_in_degree.pop(0)
            stack.append(node)
            for child_node in graph[node]:
                in_degrees[child_node] -= 1
                if in_degrees[child_node] == 0:
                    zero_in_degree.append(child_node)
        if len(stack) != len(in_degrees):
            raise ValueError('Cycle exists')     
        return stack # return topological order
    
inputs = [
    ["baa", "abcd", "abca", "cab", "cad"],
    ["ba", "bc", "ac", "cab"],
    ["cab", "aaa", "aab"],
    ["ywx", "wz", "xww", "xz", "zyy", "zwz"],
]

def main():
    for input in inputs:
        print("Character order: " + find_order(input))
        print(">>>>", Solution.alien_order(input))


main()
