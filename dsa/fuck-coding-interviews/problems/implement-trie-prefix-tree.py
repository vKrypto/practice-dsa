# coding: utf-8
"""
https://leetcode.com/problems/implement-trie-prefix-tree/s
"""
from typing import Dict
from bisect import insort, bisect_left

# There is another implementation without the intermediate node class:
# https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/trees/trie.py


class Node:

    def __init__(self, key=None):
        self.key = key
        self.children = {} # {char: node.}
        self.is_last_word = False


class Trie:

    def __init__(self):
        self.head = Node()
        

    def insert(self, word: str) -> None:
        head = self.head
        for char in word:
            if not head.children.get(char):
                temp_node = Node(key=char)
                head.children[char] = temp_node
            else:
                temp_node = head.children[char]
            head = temp_node
        head.is_last_word = True

    def search(self, word: str) -> bool:
        head = self.head
        for char in word:
            if not head.children.get(char):
                return False
            else:
                temp_node = head.children[char]
            head = temp_node
        return head.is_last_word == True
        

    def startsWith(self, prefix: str) -> bool:
        head = self.head
        for char in prefix:
            if not head.children.get(char):
                return False
            else:
                temp_node = head.children[char]
            head = temp_node
        return True


class Trie:

    def __init__(self):
        self.words = set()
        self.sorted_words = []
        
    def insert(self, word: str) -> None:
        self.words.add(word)
        insort(self.sorted_words, word)

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        index = bisect_left(self.sorted_words, prefix)
        if index == len(self.sorted_words):
            return False
        return self.sorted_words[index].startswith(prefix)
    

import collections

class Trie:

    def __init__(self):
        self.trie = collections.defaultdict()
        
    def insert(self, word: str) -> None:
        trie = self.trie
        for char in word:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]

        trie['isWord'] = True

    def search(self, word: str) -> bool:
        trie = self.trie
        for char in word:
            if char not in trie:
                return False
            trie = trie[char]
        
        if 'isWord' not in trie:
            return False
        return trie['isWord']
        

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for char in prefix:
            if char not in trie:
                return False
            trie = trie[char]
        return True
        
