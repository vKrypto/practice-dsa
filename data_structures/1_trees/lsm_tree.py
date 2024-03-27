class LSMTree:
    def __init__(self, memtable_size=4):
        self.memtable_size = memtable_size
        self.memtable = {}
        self.levels = [[]]

    def insert(self, key, value):
        self.memtable[key] = value

        if len(self.memtable) >= self.memtable_size:
            self.flush_memtable()

    def flush_memtable(self):
        sorted_keys = sorted(self.memtable.keys())
        level_idx = 0

        while level_idx < len(self.levels) and len(self.levels[level_idx]) > 0:
            sorted_keys += self.levels[level_idx]
            self.levels[level_idx] = []
            level_idx += 1

        self.levels = [sorted_keys] + self.levels[:-1]
        self.memtable = {}

    def get(self, key):
        # Search in memtable
        if key in self.memtable:
            return self.memtable[key]

        # Search in levels
        for level in self.levels:
            if key in level:
                return key

        return None


# Example usage
lsm_tree = LSMTree(memtable_size=3)

# Insert some key-value pairs
lsm_tree.insert("apple", "red")
lsm_tree.insert("banana", "yellow")
lsm_tree.insert("grape", "purple")
lsm_tree.insert("orange", "orange")

# Retrieve values
print(lsm_tree.get("apple"))    # Output: red
print(lsm_tree.get("banana"))   # Output: yellow
print(lsm_tree.get("grape"))    # Output: purple
print(lsm_tree.get("orange"))   # Output: orange
print(lsm_tree.get("watermelon"))  # Output: None
