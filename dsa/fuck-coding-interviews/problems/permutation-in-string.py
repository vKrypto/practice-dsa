# https://leetcode.com/problems/permutation-in-string/description/
from collections import Counter, defaultdict

class Solution:
    # time o(m*n), space = o(n*m) where m = len(s2), n=len(s1)
    def checkInclusion_sliding_window(self, s1: str, s2: str) -> bool:
        """
        method 1: sliding window:
        """
        char_map_s1 = Counter(s1)
        len_s1 = len(s1)
        for i in range(0, len(s2)-len_s1+1):
            char_map_window = Counter(s2[i:i+len_s1])
            if char_map_window == char_map_s1:
                return True
        return False
    
    @staticmethod
    def _counter(s:str) -> dict:
        char_map = defaultdict(int)
        for i in s:
            char_map[i] += 1
        return char_map
    
    # time o(m*n), space = o(26*2) where m = len(s2), n=len(s1)
    def checkInclusion_sliding_window_optimize_1(self, s1: str, s2: str) -> bool:
        """
        method 2: sliding window optimized_1
        # todo: Do not use Counter() logic multiple time.
        """
        len_s1 = len(s1)
        len_s2 = len(s2)

        # base case
        if len_s1 > len_s2:
            return False

        char_map_s1 = self._counter(s1)
        char_map_s2 = self._counter(s2[:len_s1])

        # linear time loop with window
        for j in range(len_s1, len_s2):
            # step 1: compare current window 
            # to-do you can avoid this and do in constant time
            if char_map_s2 == char_map_s1:
                return True

            # step 2: add last_char in char_map
            last_char = s2[j]
            char_map_s2[last_char] += 1
            
            # steop 3: decrement/remove first_char in char_map
            first_char = s2[j-len_s1]
            char_map_s2[first_char] -= 1
            if char_map_s2[first_char] < 1:
                del char_map_s2[first_char]

        return char_map_s2 == char_map_s1

    # time o(m-n), space = o(min(26, n)) where m = len(s2), n=len(s1)
    def checkInclusion_sliding_window_optimize_2(self, s1: str, s2: str) -> bool:
        """
        method 3: sliding window optimized_2
        """
        len_s1 = len(s1)
        len_s2 = len(s2)

        # base case
        if len_s1 > len_s2:
            return False

        # calcualte first window counter_maps
        char_map_s2 = {}
        char_map_s1 = {}
        for i in range(len_s1):
            char_map_s1[s1[i]] = char_map_s1.get(s1[i], 0) + 1        
            char_map_s2[s2[i]] = char_map_s2.get(s2[i], 0) + 1

        # check how many item matches in first window
        matches=0
        for char, count in char_map_s1.items():
            matches += min(count, char_map_s2.get(char, 0))

        # scroll window till the last.
        for j in range(len_s1, len_s2):
            # base-condition: check if all char matches. in s2 
            if matches == len_s1:
                return True

            last_char = s2[j] # add this char to window
            first_char = s2[j-len_s1] # remove this char to window

            # step 1: add last_char in char_map
            char_map_s2[last_char] = char_map_s2.get(last_char, 0) + 1

            # adjust matches_counter for new char            
            if char_map_s1.get(last_char) and char_map_s2[last_char] <= char_map_s1[last_char]:
                matches += 1
            # adjust matches_counter for remove char            
            if char_map_s1.get(first_char) and char_map_s1[first_char] >= char_map_s2[first_char]:
                matches -= 1
            
            # step 3: decrement/remove first_char in char_map
            char_map_s2[first_char] -= 1
            if char_map_s2[first_char] < 1:
                del char_map_s2[first_char]

        return matches == len_s1