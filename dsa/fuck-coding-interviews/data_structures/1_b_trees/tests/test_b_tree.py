# coding: utf-8
import random
import unittest

import bisect
import math


# This implementation does not support duplicate keys.
class BTreeNode:
    __slots__ = ['tree', 'parent', 'keys', 'data', '_children']

    def __init__(self, tree, parent=None):
        self.tree = tree
        self.parent = parent
        self.keys = []
        self.data = {}
        self._children = []

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, new_children):
        self._children = []
        for child in new_children:
            child.parent = self
            self._children.append(child)

    def __repr__(self):
        node_name = 'internal'
        if self.is_root():
            node_name = 'root'
        else:
            if self.is_leaf():
                node_name = 'leaf'

        return f'BTreeNode({node_name}, {self.keys})'

    def __str__(self):
        return self.__repr__()

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return not self.children

    def is_overflow(self):
        return len(self.keys) > self.tree.order - 1

    def is_underflow(self):
        if self.is_root():
            if self.is_leaf():
                return False
            else:
                return len(self.keys) < 2 - 1

        return len(self.keys) < math.ceil(self.tree.order / 2) - 1

    def split(self):
        if self.is_root():
            new_root = self.__class__(tree=self.tree, parent=None)
            self.tree.root = new_root
            self.parent = new_root
            self.parent.children = [self, ]

        median_index = (0 + len(self.keys) - 1) // 2
        median_key = self.keys[median_index]
        median_value = self.data.pop(median_key)

        new_right = self.__class__(tree=self.tree, parent=self.parent)
        new_right.keys = self.keys[median_index + 1:]
        new_right.children = self.children[median_index + 1:]
        for key in new_right.keys:
            new_right.data[key] = self.data.pop(key)

        self.keys = self.keys[:median_index]
        self.children = self.children[:median_index + 1]  # NOTE: Here is "median_index + 1" instead of "median_index".

        child_index = self.parent.children.index(self)
        self.parent.children.insert(child_index + 1, new_right)
        self.parent.insert(key=median_key, value=median_value)

    def insert(self, key, value):
        bisect.insort_left(self.keys, key)
        self.data[key] = value
        if self.is_overflow():
            self.split()

    def rotate_right(self):  # Borrow a key from the left sibling.
        my_index = self.parent.children.index(self)
        if my_index == 0:  # There is no left sibling.
            return False

        separator_index = my_index - 1
        left_sibling_index = my_index - 1
        left_sibling = self.parent.children[left_sibling_index]
        if len(left_sibling.keys) <= math.ceil(self.tree.order / 2) - 1:
            return False

        separator = self.parent.keys[separator_index]
        self.keys.insert(0, separator)
        self.data[separator] = self.parent.data.pop(separator)
        self.parent.keys[separator_index] = key = left_sibling.keys.pop()
        self.parent.data[key] = left_sibling.data.pop(key)

        if not self.is_leaf():  # Since we borrow a key from the left sibling, the corresponding child node of the key should also be moved.
            child = left_sibling.children.pop()
            child.parent = self
            self.children.insert(0, child)

        return True

    def rotate_left(self):
        my_index = self.parent.children.index(self)
        if my_index == len(self.parent.children) - 1:
            return False

        separator_index = my_index
        right_sibling_index = my_index + 1
        right_sibling = self.parent.children[right_sibling_index]
        if len(right_sibling.keys) <= math.ceil(self.tree.order / 2) - 1:
            return False

        separator = self.parent.keys[separator_index]
        self.keys.append(separator)
        self.data[separator] = self.parent.data.pop(separator)
        self.parent.keys[separator_index] = key = right_sibling.keys.pop(0)
        self.parent.data[key] = right_sibling.data.pop(key)

        if not self.is_leaf():
            child = right_sibling.children.pop(0)
            child.parent = self
            self.children.append(child)

        return True

    def merge_left(self):  # Merge the left sibling into the current node.
        my_index = self.parent.children.index(self)
        if my_index == 0:
            return False

        left_sibling_index = my_index - 1
        left_sibling = self.parent.children[left_sibling_index]
        if len(left_sibling.keys) != math.ceil(self.tree.order / 2) - 1:  # We can only merge a sibling which has exactly the minimum number of keys.
            return False

        # Copy the separator from the parent to the end of the left node.
        # Move the left sibling's keys and children to the current node.
        separator_index = my_index - 1
        separator = self.parent.keys[separator_index]
        self.keys = left_sibling.keys + [separator, ] + self.keys
        self.children = left_sibling.children + self.children
        self.data[separator] = self.parent.data.pop(separator)
        for key in left_sibling.keys:
            self.data[key] = left_sibling.data.pop(key)

        # Remove the separator from the parent along with its empty right child.
        self.parent.keys.pop(separator_index)
        self.parent.children.pop(left_sibling_index)

        if self.parent.is_underflow():
            self.parent.rebalance()

        return True

    def merge_right(self):
        my_index = self.parent.children.index(self)
        if my_index == len(self.parent.children) - 1:
            return False

        right_sibling_index = my_index + 1
        right_sibling = self.parent.children[right_sibling_index]
        if len(right_sibling.keys) != math.ceil(self.tree.order / 2) - 1:
            return False

        separator_index = my_index
        separator = self.parent.keys[separator_index]
        self.keys = self.keys + [separator, ] + right_sibling.keys
        self.children = self.children + right_sibling.children
        self.data[separator] = self.parent.data.pop(separator)
        for key in right_sibling.keys:
            self.data[key] = right_sibling.data.pop(key)

        self.parent.keys.pop(separator_index)
        self.parent.children.pop(right_sibling_index)

        if self.parent.is_underflow():
            self.parent.rebalance()

        return True

    def rebalance(self):
        """
        First, we borrow a key from both immediate sibling nodes in the order of left and right.

        If both immediate sibling nodes already have a minimum number of keys,
        then we merge the left or right sibling into the current node.

        https://en.wikipedia.org/wiki/B-tree#Rebalancing_after_deletion
        """
        if self.is_root():
            # If we land here, the root node has no keys but one child node.
            # So we promote the only child as the new root.
            new_root = self.children[0]
            new_root.parent = None
            self.tree.root = new_root
            return True

        assert \
            self.rotate_right() or self.rotate_left() or \
            self.merge_left() or self.merge_right()

    def delete(self, key):
        if self.is_leaf():
            self.keys.remove(key)
            self.data.pop(key)
            if self.is_underflow():
                self.rebalance()
        else:
            index = self.keys.index(key)
            node = self.children[index]  # The left subtree.
            while not node.is_leaf():
                node = node.children[-1]

            new_separator = node.keys[-1]  # Choose the largest key in the left subtree as the new separator.
            del self.data[self.keys[index]]
            self.keys[index] = new_separator  # Replace the key to be deleted with the new separator.
            self.data[new_separator] = node.data[new_separator]  # Replace the key to be deleted with the new separator.
            node.delete(new_separator)  # Delete the new separator from the leaf node.

    def check_validation(self):
        """
        According to Knuth's definition, a B-tree of order m is a tree which satisfies the following properties:

        - Every node has at most m children.
        - Every non-leaf node (except root) has at least ⌈m/2⌉ child nodes.
        - The root has at least 2 children if it is not a leaf node.
        - A non-leaf node with k children contains k − 1 keys.
        - All leaves appear in the same level and carry no information.

        https://en.wikipedia.org/wiki/B-tree#Definition
        """
        if len(self.tree):
            assert self.keys
            assert self.keys == sorted(self.keys)
            assert set(self.keys) == set(self.data.keys())

        num_children = len(self.children)
        assert num_children <= self.tree.order, num_children

        if not self.is_leaf() and not self.is_root():  # Internal nodes.
            assert num_children >= math.ceil(self.tree.order / 2), num_children

        if self.is_root() and not self.is_leaf():
            assert num_children >= 2, num_children

        if not self.is_leaf():
            assert num_children - 1 == len(self.keys), num_children

        for child in self.children:
            assert child.parent == self
            child.check_validation()


class BTree:
    NODE_CLASS = BTreeNode
    DEFAULT_TO_ROOT = object()

    def __init__(self, order=512):
        if order < 3:
            raise ValueError('order must be greater than or equal to 3')

        self._size = 0
        self.order = order
        self.root = self.NODE_CLASS(tree=self)

    def __len__(self):
        return self._size

    def __iter__(self):
        yield from self.inorder_traverse_keys()

    def __repr__(self) -> str:
        print(".")
        # nodes = list(self.levelorder_traverse_nodes())
        nodes = []

        current_level = [self.root, ]
        while current_level:
            print([node.keys for node in current_level])
            next_level = []
            for node in current_level: 
                next_level.extend(node.children)
            nodes.append(next_level)
            current_level = next_level
        return ""

    def search_node(self, key, node):
        index = bisect.bisect_left(node.keys, key)
        try:
            if node.keys[index] == key:
                return node, index
        except IndexError:
            pass

        if node.is_leaf():
            return node, -1
        else:
            return self.search_node(key, node.children[index])

    def get(self, key):
        node, index = self.search_node(key, self.root)
        if index == -1:
            raise KeyError

        return node.data[key]

    def insert(self, key, value):
        node, index = self.search_node(key, self.root)
        if index != -1:
            raise KeyError('Duplicate key')

        node.insert(key, value)
        self._size += 1

    def delete(self, key):
        node, index = self.search_node(key, self.root)
        if index == -1:
            raise KeyError

        node.delete(key)
        self._size -= 1

    def num_nodes(self):
        count = 0
        for _ in self.levelorder_traverse_nodes():
            count += 1
        return count

    def min(self, node=DEFAULT_TO_ROOT):
        if node == self.DEFAULT_TO_ROOT:
            node = self.root

        if node.is_leaf():
            key = node.keys[0]
            return {'key': key, 'value': node.data[key]}
        else:
            return self.min(node.children[0])

    def max(self, node=DEFAULT_TO_ROOT):
        if node == self.DEFAULT_TO_ROOT:
            node = self.root

        if node.is_leaf():
            key = node.keys[-1]
            return {'key': key, 'value': node.data[key]}
        else:
            return self.max(node.children[-1])

    def inorder_traverse_keys(self, node=DEFAULT_TO_ROOT):
        if node == self.DEFAULT_TO_ROOT:
            node = self.root

        if node.is_leaf():
            yield from node.keys
            return

        key_length = len(node.keys)
        for i, left_child_node in enumerate(node.children):
            yield from self.inorder_traverse_keys(left_child_node)
            if i < key_length:
                yield node.keys[i]

    def levelorder_traverse_nodes(self, node=DEFAULT_TO_ROOT):
        if node == self.DEFAULT_TO_ROOT:
            node = self.root

        current_level = [self.root, ]
        while current_level:
            next_level = []
            for node in current_level:
                yield node
                next_level.extend(node.children)

            current_level = next_level




b_t = BTree(order=5)
for i in [2,5,8,9,78,45,65,12,48]:
    print(b_t)
    b_t.insert(key=i, value=f'{i}')
print(b_t)

class BTreeTest(unittest.TestCase):
    def setUp(self):
        with self.assertRaises(ValueError):
            BTree(order=2)

        self.b_tree = BTree(order=5)
        self.size = random.randint(1, 1000)
        self.keys = random.sample(range(1000), k=self.size)
        for i in self.keys:
            self.b_tree.insert(key=i, value=f'{i}')

    def test__len__(self):
        self.assertEqual(len(self.b_tree), self.size)

    def test__iter__(self):
        self.assertEqual(list(self.b_tree), sorted(self.keys))

    def test_get(self):
        for key in self.keys:
            self.assertEqual(self.b_tree.get(key), f'{key}')

        with self.assertRaises(KeyError):
            self.b_tree.get(-1)

    def test_insert(self):
        b_tree = BTree(order=3)

        b_tree.insert(key=42, value='42')
        self.assertEqual(b_tree.root.keys, [42, ])
        self.assertEqual(b_tree.root.children, [])

        b_tree.insert(key=11, value='11')
        self.assertEqual(b_tree.root.keys, [11, 42])
        self.assertEqual(b_tree.root.children, [])

        b_tree.insert(key=27, value='27')
        self.assertEqual(b_tree.root.keys, [27, ])
        self.assertEqual([node.keys for node in b_tree.root.children], [[11, ], [42, ]])

        b_tree.insert(key=4, value='4')
        self.assertEqual(b_tree.root.keys, [27, ])
        self.assertEqual([node.keys for node in b_tree.root.children], [[4, 11], [42, ]])

        b_tree.insert(key=8, value='8')
        self.assertEqual(b_tree.root.keys, [8, 27])
        self.assertEqual([node.keys for node in b_tree.root.children], [[4], [11], [42]])

        b_tree.insert(key=16, value='16')
        self.assertEqual(b_tree.root.keys, [8, 27])
        self.assertEqual([node.keys for node in b_tree.root.children], [[4], [11, 16], [42]])

        b_tree.insert(key=23, value='23')
        self.assertEqual(b_tree.root.keys, [16, ])
        self.assertEqual([node.keys for node in b_tree.root.children], [[8], [27]])
        self.assertEqual([node.keys for node in b_tree.root.children[0].children], [[4], [11]])
        self.assertEqual([node.keys for node in b_tree.root.children[1].children], [[23], [42]])

        with self.assertRaises(KeyError):
            b_tree.insert(23, '23')

        self.assertEqual(list(b_tree), [4, 8, 11, 16, 23, 27, 42])
        self.assertEqual(len(b_tree), 7)
        self.assertEqual(b_tree.num_nodes(), 7)

    def test_delete(self):
        b_tree = BTree(order=3)
        b_tree.insert(key=42, value='42')
        b_tree.insert(key=11, value='11')
        b_tree.insert(key=27, value='27')
        b_tree.insert(key=4, value='4')
        b_tree.insert(key=8, value='8')
        b_tree.insert(key=16, value='16')
        b_tree.insert(key=23, value='23')
        print(b_tree)

        with self.assertRaises(KeyError):
            b_tree.delete(0)

        b_tree.delete(key=16)
        self.assertEqual(b_tree.root.keys, [11, 27])
        self.assertEqual([node.keys for node in b_tree.root.children], [[4, 8], [23], [42]])

        b_tree.delete(key=4)
        self.assertEqual(b_tree.root.keys, [11, 27])
        self.assertEqual([node.keys for node in b_tree.root.children], [[8], [23], [42]])

        b_tree.delete(key=11)
        self.assertEqual(b_tree.root.keys, [27])
        self.assertEqual([node.keys for node in b_tree.root.children], [[8, 23], [42]])

        b_tree.delete(key=23)
        self.assertEqual(b_tree.root.keys, [27])
        self.assertEqual([node.keys for node in b_tree.root.children], [[8], [42]])

        b_tree.delete(key=8)
        self.assertEqual(b_tree.root.keys, [27, 42])

        b_tree.delete(key=42)
        self.assertEqual(b_tree.root.keys, [27])

        b_tree.delete(key=27)
        self.assertEqual(b_tree.root.keys, [])

        self.assertEqual(len(b_tree), 0)
        self.assertEqual(list(b_tree), [])

    def test_min(self):
        self.assertEqual(self.b_tree.min()['key'], min(self.keys))

    def test_max(self):
        self.assertEqual(self.b_tree.max()['key'], max(self.keys))

    def test_check_validation(self):
        order = random.randint(3, 64)
        size = random.randint(1, 5000)

        with self.subTest(order=order, size=size):
            b_tree = BTree(order=order)
            keys = random.sample(range(5000), k=size)
            self.assertEqual(len(keys), len(set(keys)))

            inserted_keys = []
            for i in keys:
                b_tree.insert(key=i, value=f'{i}')
                inserted_keys.append(i)

                if random.randint(1, 10) % 3 == 0:
                    random_index = random.randint(0, len(inserted_keys) - 1)
                    delete_key = inserted_keys.pop(random_index)
                    b_tree.delete(delete_key)

                for node in b_tree.levelorder_traverse_nodes():
                    node.check_validation()

            self.assertEqual(list(b_tree), sorted(inserted_keys))

            for i in inserted_keys:
                b_tree.delete(i)

                for node in b_tree.levelorder_traverse_nodes():
                    node.check_validation()

            self.assertEqual(len(b_tree), 0)
            self.assertEqual(list(b_tree), [])
            self.assertEqual(b_tree.num_nodes(), 1)  # An empty root node.


if __name__ == '__main__':
    # unittest.main()
    ...
