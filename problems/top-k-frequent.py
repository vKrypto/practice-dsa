# https://leetcode.com/problems/top-k-frequent-words/description/

from typing import List
from collections import Counter
from heapq import heapify


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq=Counter(words)
        temp=sorted(freq.items(),key=lambda v:(-v[1], v[0]))
        res=[]
        for i in range(k):
            res.append(temp[i][0])
        return res
    
    
    
    def topKFrequent2(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        h = [(-value, key) for key, value in c.items()]
        
        heapify(h)
        h.sort(key = lambda x: (x[0], x[1]))
        
        return [x for _, x in h[:k]]
    
    # time: O(n), space: O(n)
    def topKFrequent3(self, words: List[str], k: int) -> List[str]:
        from collections import defaultdict
        freq = defaultdict(int)
        for word in words:
            freq[word] += 1
        groups = [[] for _ in range(len(words))]
        for word,frequency in freq.items():
            groups[frequency].append(word)
        sorted_words = []
        for group in groups[::-1]:
            for word in group:
                sorted_words.append(word)
                if len(sorted_words)== k:
                    return sorted_words            
        return sorted_words   