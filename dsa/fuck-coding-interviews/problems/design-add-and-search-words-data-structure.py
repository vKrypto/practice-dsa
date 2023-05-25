# https://leetcode.com/problems/design-add-and-search-words-data-structure
# extension of https://leetcode.com/problems/implement-trie-prefix-tree

from . import collections

class Node:
    __slots__ = ('key', 'children', 'is_last_word')
    def __init__(self, key=None, parent=None):
        self.key = key
        self.children = {} # {char: node.}
        self.is_last_word = False


class WordDictionary:

    def __init__(self):
        self.head = Node()
        

    def addWord(self, word: str) -> None:
        head = self.head
        for char in word:
            if not head.children.get(char):
                temp_node = Node(key=char)
                head.children[char] = temp_node
            else:
                temp_node = head.children[char]
            head = temp_node
        head.is_last_word = True

    def search(self, word: str, head=None) -> bool:
        head = head or self.head
        for index, char in enumerate(word):
            # split problem into loops.
            if char == ".":
                for node in head.children.values():
                    is_matched = self.search(word[index+1:], head=node)
                    if is_matched:
                        return True
                return False

            if not head.children.get(char):
                return False
            temp_node = head.children[char]
            head = temp_node
        return head.is_last_word == True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# much faster than above solutions
class WordDictionary:

    def __init__(self):
        self.trie = collections.defaultdict()
        
    def addWord(self, word: str) -> None:
        trie = self.trie
        for char in word:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]

        trie['isWord'] = True

    def search(self, word: str, head=None) -> bool:
        trie = head or self.trie
        for i, char in enumerate(word):
            # split problem into loops.
            if char == ".":
                for node in trie.values():
                    if isinstance(node, bool):
                        continue
                    is_matched = self.search(word[i+1:], head=node)
                    if is_matched:
                        return True
                return False
            if char not in trie:
                return False
            trie = trie[char]
        if 'isWord' not in trie:
            return False
        return trie['isWord']
