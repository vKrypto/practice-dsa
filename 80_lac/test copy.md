# Senior/Staff Engineer DSA Interview Questions (with Examples & Why)

---

## 1. Sliding Window Maximum

**Question:**  
Given an array of integers and a window size `k`, find the maximum for each sliding window of size `k`.

**Why?**  
Tests understanding of monotonic queues, deque usage, and space/time trade-offs.

**Input:**  
`nums = [1, 3, -1, -3, 5, 3, 6, 7]`, `k = 3`

**Output:**  
`[3, 3, 5, 5, 6, 7]`

---

## 2. LRU Cache Implementation

**Question:**  
Design and implement an LRU (Least Recently Used) Cache with O(1) `get` and `put`.

**Why?**  
Evaluates hash map + double-linked list combo, data structure design, and real-world cache understanding.

**Input:**  
Operations: `["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]`  
Arguments: `[[2], [1,1], [2,2], [1], [3,3], [2], [4,4], [1], [3], [4]]`

**Output:**  
`[null, null, null, 1, null, -1, null, -1, 3, 4]`

---

## 3. Kth Largest Element in a Data Stream

**Question:**  
Given a stream of integers, design a class to return the kth largest element at any point.

**Why?**  
Heap operations, continuous input handling, and dynamic datasets.

**Input:**  
Initialize: `k = 3`, `nums = [4, 5, 8, 2]`  
Operations: `add(3)`, `add(5)`, `add(10)`, `add(9)`, `add(4)`

**Output:**  
`4, 5, 5, 8, 8`

---

## 4. Find All Anagrams in a String

**Question:**  
Given a string `s` and a pattern `p`, find all the start indices of p's anagrams in s.

**Why?**  
Efficient substring search, hash maps, sliding window mastery.

**Input:**  
`s = "cbaebabacd"`, `p = "abc"`

**Output:**  
`[0, 6]`

---

## 5. Union-Find (Disjoint Set) With Path Compression and Union by Rank

**Question:**  
Implement a disjoint set data structure supporting union and find operations efficiently.

**Why?**  
Real system problems—network connectivity, cycle detection in graphs, etc.

**Input:**  
`n = 5`  
Operations: `union(0,1)`, `union(1,2)`, `find(2)`, `find(3)`, `union(3,4)`, `find(4)`

**Output:**  
`True, True, 0, 3, True, 3`

---

## 6. Top K Frequent Elements

**Question:**  
Given a non-empty array of integers, return the k most frequent elements.

**Why?**  
Heap vs bucket sort, frequency maps—think log-linear optimizations.

**Input:**  
`nums = [1,1,1,2,2,3]`, `k = 2`

**Output:**  
`[1, 2]`  
*(Order may vary)*

---

## 7. Longest Substring Without Repeating Characters

**Question:**  
Given a string, find the length of the longest substring without repeating characters.

**Why?**  
Classic windowing, set/hash map knowledge, edge cases.

**Input:**  
`s = "abcabcbb"`

**Output:**  
`3`

---

## 8. Minimum Spanning Tree (MST) in a Graph

**Question:**  
Given an undirected weighted graph, implement an algorithm to find its Minimum Spanning Tree.

**Why?**  
Real-world systems (network design), must know Kruskal’s/Prim’s algorithm.

**Input:**  
`n = 4, edges = [[0,1,1], [0,2,2], [1,2,2], [1,3,1], [2,3,2]]`

**Output:**  
`3`  
*(Sum of MST weights)*

---

## 9. Serialize and Deserialize a Binary Tree

**Question:**  
Design an algorithm to serialize and deserialize a binary tree.

**Why?**  
Tree traversal, recursion/iteration, data encoding.

**Input:**  
Tree:  
```
    1
   / \
  2   3
     / \
    4   5

```


**Output:**  
Serialized: `"1,2,#,#,3,4,#,#,5,#,#"`  
*(Format may vary)*

---

## 10. Median of Two Sorted Arrays

**Question:**  
Given two sorted arrays, find the median of the combined sorted array in O(log(min(n, m))) time.

**Why?**  
Binary search with edge case handling, true mastery-level array problem.

**Input:**  
`nums1 = [1, 3]`, `nums2 = [2]`

**Output:**  
`2.0`

---

## 11. Cycle Detection in Directed and Undirected Graph

**Question:**  
Given a graph, detect if it contains a cycle.

**Why?**  
DFS, parent tracking, graph traversal patterns.

**Input:**  
Undirected: `n = 4, edges = [[0,1], [1,2], [2,3], [3,0]]`

**Output:**  
`True`

---

## 12. Largest Rectangle in Histogram

**Question:**  
Given an array representing the histogram’s bar height, find the area of the largest rectangle.

**Why?**  
Stack usage, tricky edge cases, O(n) solution required.

**Input:**  
`heights = [2,1,5,6,2,3]`

**Output:**  
`10`

---

## 13. Word Ladder / Shortest Transformation Sequence

**Question:**  
Given a start word, end word, and a dictionary, transform the start word to the end word with the shortest sequence (one letter at a time, intermediate words must exist in the dictionary).

**Why?**  
BFS/DFS, path finding, set operations.

**Input:**  
`beginWord = "hit"`, `endWord = "cog"`, `wordList = ["hot","dot","dog","lot","log","cog"]`

**Output:**  
`5`  
*(hit → hot → dot → dog → cog)*

---

## 14. Kth Smallest/Largest in BST

**Question:**  
Given a Binary Search Tree, find the kth smallest (or largest) element.

**Why?**  
Tree traversal, recursion, augmenting data structures.

**Input:**  
BST: `[3,1,4,null,2]`, `k = 1`

**Output:**  
`1`

---

## 15. Find Missing Number in a Range

**Question:**  
Given an array containing n distinct numbers from 0 to n, find the one number that is missing.

**Why?**  
Bit manipulation or simple arithmetic, optimal in-place solution.

**Input:**  
`nums = [3,0,1]`

**Output:**  
`2`

---



---

## 16. Course Schedule (Detect Cycle in Prerequisites)

**Question:**  
Given `numCourses` and a list of prerequisite pairs, determine if you can finish all courses (no cyclic dependencies).

**Why?**  
Topological sort, cycle detection in directed graphs—core for dependency resolution.

**Input:**  
`numCourses = 4`, `prerequisites = [[1,0],[2,1],[3,2]]`

**Output:**  
`True`

---

## 17. Merge Intervals

**Question:**  
Given a collection of intervals, merge all overlapping intervals.

**Why?**  
Interval handling, sorting, and edge case management.

**Input:**  
`intervals = [[1,3],[2,6],[8,10],[15,18]]`

**Output:**  
`[[1,6],[8,10],[15,18]]`

---

## 18. Trapping Rain Water

**Question:**  
Given n non-negative integers representing elevation, compute how much water it can trap after raining.

**Why?**  
Pointer manipulation, array traversal, optimization.

**Input:**  
`height = [0,1,0,2,1,0,1,3,2,1,2,1]`

**Output:**  
`6`

---

## 19. Number of Islands

**Question:**  
Given a 2D grid of '1's (land) and '0's (water), count the number of islands.

**Why?**  
DFS/BFS, grid traversal, connected component analysis.

**Input:**  
`grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]`

**Output:**  
`3`

---

## 20. Subarray Sum Equals K

**Question:**  
Given an array of integers and an integer k, find the total number of continuous subarrays whose sum equals to k.

**Why?**  
Prefix sums, hash map optimization, real-world analytics.

**Input:**  
`nums = [1,1,1]`, `k = 2`

**Output:**  
`2`

---

## 21. Longest Palindromic Substring

**Question:**  
Given a string s, find the longest palindromic substring in s.

**Why?**  
String manipulation, expand around center, DP optimization.

**Input:**  
`s = "babad"`

**Output:**  
`"bab"` or `"aba"`

---

## 22. Rotate Image (Matrix)

**Question:**  
Given an n x n 2D matrix, rotate it 90 degrees clockwise in-place.

**Why?**  
In-place matrix manipulation, 2D array transformations.

**Input:**  
`matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]`

**Output:**  
`[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]`

---

## 23. Product of Array Except Self

**Question:**  
Given an integer array nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].  
*Solve it without division and in O(n).*

**Why?**  
Prefix/postfix computation, O(1) extra space challenge.

**Input:**  
`nums = [1,2,3,4]`

**Output:**  
`[24,12,8,6]`

---

## 24. Find Peak Element

**Question:**  
A peak element is one that is greater than its neighbors. Given an array, find a peak element and return its index.

**Why?**  
Binary search application beyond sorted arrays, edge handling.

**Input:**  
`nums = [1,2,3,1]`

**Output:**  
`2`  *(nums[2] = 3 is a peak)*

---

## 25. Clone Graph

**Question:**  
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

**Why?**  
Graph traversal, hash maps for visited nodes, real-world cloning/copying.

**Input:**  
Graph with nodes and edges:  
`[[2,4],[1,3],[2,4],[1,3]]`  
*(Adjacency list for node 1: [2,4], node 2: [1,3], ...)*

**Output:**  
A cloned graph represented in the same adjacency list format.

---
