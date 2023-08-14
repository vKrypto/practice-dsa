# coding: utf-8
"""
Trie
https://en.wikipedia.org/wiki/Trie
"""


class Trie:
    def __init__(self):
        self.root = {}
        self.size = 0

    def __len__(self):
        return self.size

    def insert(self, word: str) -> None:
        if not word:
            raise ValueError('word cannot be empty')

        node = self.root
        for char in word:
            node = node.setdefault(char, {})

        # Since the searched word might be shorter than the word in Trie,
        # search() needs a way to determine whether the searching matches the exact word,
        # For instance, we have `hammer`in Trie and we are searching for `hammers` which should return False.
        node['$word_end'] = True
        self.size += 1

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            try:
                node = node[char]
            except KeyError:
                return False

        if '$word_end' in node:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            try:
                node = node[char]
            except KeyError:
                return False

        return True
