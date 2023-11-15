"""

input: = [["g", "c", "a"], ["f", "c", "a"], ["e", "b", "a"], ["d", "b", "a"]] 

input_data array [n * h] represents traversals form child to parent.
input stream : ["a", "green"], ["d", "yellow"] ,["b", "blue"], ["a", "red"], ....


write a program where you need apply color to a node and it's child nodes (using input stream), unless some color is already applied to a child node by it's in-between parent or itself


output : print the final color of each node
"""

#   a
#  a  a
# a a a a

#     a
#   c    b
# g f  e  d

"""

input: = [["g", "c", "a"], ["f", "c", "a"], ["e", "b", "a"], ["d", "b", "a"]] 

input_data array [n * h] represents traversals form child to parent.
input stream : ["a", "green"], ["d", "yellow"] ,["b", "blue"], ["a", "red"]


write a program where you need apply color to a node and it's child nodes unless some color is already applied to a child node by it's in-between parent or itself


output : print the final color of each node
"""

#   a
#  a  a
# a a a a

#     a
#   c    b
# g f  e  d


# output_format = {
#     "a": "red",
#     "b": "blue",
#     "c": "red",
#     "d": "yellow",
#     "e": "blue",
#     "f": "red",
#     "g": "red",
# }



class TreeNode:

    def __init__(self, val, color=None):
        self.val = val
        self.color = color
        self.left = None
        self.right = None
        

class Solution:
    
    hash_map = {} # {"a": TreeNode}

    def build_tree(self, input_paths):
        for path in input_paths:
            child_node = TreeNode(path[0])

            self.hash_map[path[0]] = child_node

            for node_val in path[1:]:
                temp = self.hash_map.get(node_val, TreeNode(node_val))

                self.hash_map[node_val] = temp

                if temp.left is None:
                    temp.left = child_node
                else:
                    temp.right = child_node

                child_node = temp

    def assign_colors(self, input_stream):
        for node_val, node_color in input_stream:
            self.hash_map[node_val].color = node_color

    def get_color(self, input_paths, input_stream):
        self.build_tree(input_paths)
        self.assign_colors(input_stream)
        
        root = self.hash_map[input_paths[0][-1]]

        final_color = {} # {"a": color}

        def dfs(node, color=None):
            # base-case:
            if node is None:
                return
            
            color = node.color  or color
            dfs(node.left, color)
            dfs(node.right, color)
            # update color
            final_color[node.val] = color

        dfs(root)

        return final_color


input_paths = [["g", "c", "a"], ["f", "c", "a"], ["e", "b", "a"], ["d", "b", "a"]] 
input_stream = [["a", "green"], ["d", "yellow"] ,["b", "blue"], ["a", "red"]]


print(Solution().get_color(input_paths, input_stream))
