# coding: utf-8
"""
https://en.wikipedia.org/wiki/Tree_%28data_structure%29#Terminology_used_in_trees
http://typeocaml.com/2014/11/26/height-depth-and-level-of-a-tree/
"""
from abc import ABC
from abc import abstractmethod


class BaseNode(ABC):
    """
    General implementation of a TreeBaseNode
    """

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def __eq__(self, other):
        ...

    @abstractmethod
    def to_tuple_representation(self):
        ...

    @abstractmethod
    def from_tuple_representation(self):
        ...

    @abstractmethod
    def display(self):
        ...


class TreeNode(BaseNode):
    """
    General implementation of a TreeNode
    """
    __slots__ = ['value', 'left', 'right']

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.value})'

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return all((
            self.value == other.value,
            self.left == other.left,
            self.right == other.right,
        ))

    def to_tuple_representation(self) -> tuple:
        """
        convert normal Tree Node to in order tuple [left, head, right]
        """
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.value
        return self.left.to_tuple() , self.value, self.right.to_tuple()
    
    @classmethod
    def from_tuple_representation(cls, data):
        """
        """
        if isinstance(data, (tuple, list)) and len(data) == 3:
            head_node = cls(data[1])
            head_node.left = cls.from_tuple_representation(data[0])
            head_node.right = cls.from_tuple_representation(data[2])
        elif data is None:
            head_node = None
        else:
            head_node = cls(data)
        return head_node
    
    def display(self, space='\t', level=0):
        """
        """
        # If the node is empty
        if self is None:
            print(space*level + '∅')
            return   

        # If the node is a leaf 
        if self.left is None and self.right is None:
            print(space*level + str(self.value))
            return

        # If the node has children
        self.right.display(space, level+1)
        print(space*level + str(self.value))
        self.left.display(space, level+1)  


class BaseTree(ABC):
    """
    General implementation of a Tree
    """

    NODE_CLASS = BaseNode
    DEFAULT_TO_ROOT = object()

    @abstractmethod
    def __init__(self):
        self.tree = None
        self.size = 0

    @abstractmethod
    def __eq__(self, value):
        ...

    @abstractmethod
    def __len__(self):
        ...

    @abstractmethod
    def __iter__(self):
        ...

    @abstractmethod
    def __contains__(self, value):
        ...

    @abstractmethod
    def is_root(self, node):
        ...

    @abstractmethod
    def is_leaf(self, node):
        ...

    def is_external(self, node):
        return self.is_leaf(node)

    def is_internal(self, node):
        return not self.is_external(node)

    @abstractmethod
    def traverse(self):
        ...

    @abstractmethod
    def height(self, node):
        ...

    @abstractmethod
    def depth(self, node):
        ...

    @abstractmethod
    def level(self, node):
        ...

    @classmethod
    def from_array_representation(cls, array):
        """
        The index of parent node of array[i] is math.floor((i - 1) / 2).
        Also, every odd index indicates a left node, and every even index indicates a right node.
        https://learning.oreilly.com/library/view/data-structures-and/9781118290279/13_chap08.html#ch008-sec022
        """
        bst = cls()

        if not array:
            return bst

        nodes = [value if value is None else cls.NODE_CLASS(value) for value in array]
        for i in range(1, len(nodes)):
            node = nodes[i]
            parent_index = (i - 1) // 2
            parent_node = nodes[parent_index]
            if (node is None) and (parent_node is None):
                continue
            if i % 2 == 0:
                parent_node.right = nodes[i]
            else:
                parent_node.left = nodes[i]

        bst.root = nodes[0]
        return bst

    def to_array_representation(self):
        """
        Return the "Array Representation" of the tree.
        https://en.wikipedia.org/wiki/Binary_tree#Arrays
        """
        array = []
        current_level = [self.root, ]
        next_level = []
        while any(current_level):
            for node in current_level:
                # We append values to array for current_level,
                # and put their child nodes to next_level.
                if node:
                    array.append(node.value)
                    next_level.extend([node.left, node.right])
                else:
                    array.append(None)
                    next_level.extend([None, None])

            current_level = next_level
            next_level = []

        while array and (array[-1] is None):
            array.pop()

        return array

    @classmethod
    def from_tuple_representation(cls, data) -> TreeNode:
        """
        convert [left, head, right] to BinarySearchTree,
        """
        bst = cls()
        if not data:
            return bst
        bst.tree = cls.NODE_CLASS.from_tuple_representation(data)
        bst.size = len(bst)
        return bst

    def to_tuple_representation(self) -> tuple:
        """
        convert normal binary search tree to in order tuple [left, head, right]
        """
        if self.tree is None:
            return None
        if self.tree.left is None and self.tree.right is None:
            return self.tree.value
        return self.tree.to_tuple_representation()
    
    def display(self, node=DEFAULT_TO_ROOT):
        if node is self.DEFAULT_TO_ROOT:
            node = self.root
        return node.display
  