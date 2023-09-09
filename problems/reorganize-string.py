import heapq
from collections import Counter, deque


class Solution:
    
    # not passing all test cases here, wrong approach
    def reorganizeString(self, s: str) -> str:
        # modifying input : please avoid
        count_map = Counter(s)
        sorted_count_map = dict(sorted(count_map.items(), key=lambda item: item[1], reverse=True))
        s = ""
        for char, count in sorted_count_map.items():
            s += char * count

        waiting_q = deque()
        last_char = ""
        res = ""
        for char in s:
            if char == last_char:
                waiting_q.append(char)
            else:
                res += char
                last_char = char
                if waiting_q:
                    last_char = waiting_q.popleft()
                    res += last_char
        if len(waiting_q) == 1 and res[0] != waiting_q[0]:
            last_char = waiting_q.popleft()
            res = last_char + res
        return res if not waiting_q else ""



    def reorganizeString(self, s: str) -> str:
        freq_map = {}
        for char in s:
            freq_map[char] = freq_map.get(char, 0) + 1
            
        sorted_chars = sorted(freq_map.keys(), key=lambda x: freq_map[x], reverse=True)
        
        if freq_map[sorted_chars[0]] > (len(s) + 1) // 2:
            return ""
        
        res = [None] * len(s)
        
        i = 0
        for char in sorted_chars:
            for _ in range(freq_map[char]):
                if i >= len(s):
                    i = 1
                res[i] = char
                i += 2
                
        return "".join(res)
    
    
    # priority queue - optimized solution
    def reorganizeString(self, s: str) -> str:
        freq_map = {}
        for char in s:
            freq_map[char] = freq_map.get(char, 0) + 1
            
        max_heap = [(-freq, char) for char, freq in freq_map.items()]
        heapq.heapify(max_heap)
        
        res = []
        
        while len(max_heap) >= 2:
            freq1, char1 = heapq.heappop(max_heap)
            freq2, char2 = heapq.heappop(max_heap)
            
            res.extend([char1, char2])
            
            if freq1 + 1 < 0:
                heapq.heappush(max_heap, (freq1 + 1, char1))
            if freq2 + 1 < 0:
                heapq.heappush(max_heap, (freq2 + 1, char2))
                
        if max_heap:
            freq, char = heapq.heappop(max_heap)
            if -freq > 1:
                return ""
            res.append(char)
            
        return "".join(res)