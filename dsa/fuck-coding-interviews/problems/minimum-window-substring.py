import collections

class Solution:
    # time= o(len(s2)), space= 2* o(len(s1)),
    def minWindow(self, s2: str, s1: str) -> str:
        len_s1 = len(s1)
        len_s2 = len(s2)

        # base case 1: 
        if len_s1 > len_s2:
            return ""

        # calcualte first window counter_maps
        char_map_s2 =  collections.defaultdict(int)
        char_map_s1 =  collections.defaultdict(int)
        for i in range(len_s1):
            char_map_s1[s1[i]] = char_map_s1[s1[i]] + 1        
            char_map_s2[s2[i]] = char_map_s2[s2[i]] + 1

        # check how many item matches in first window
        matches=0
        for char, count in char_map_s1.items():
            matches += min(count, char_map_s2[char])
            
        # strign does matches completely, base-case 2
        if matches == len(s1):
            return s2[:len_s1]

        left = 0 
        min_res_length = float('infinity')
        min_res = ""

        # scroll window till the last.
        for j in range(len_s1, len_s2):

            # step 1: add next_char in char_map
            next_char = s2[j] # add this char to window
            char_map_s2[next_char] = char_map_s2[next_char] + 1
            if char_map_s1[next_char] and char_map_s2[next_char] <= char_map_s1[next_char]:
                matches += 1
            
            # step 2: # remove first char of current window if not required, recursviely
            first_char = s2[left] 
            while char_map_s1[first_char] < char_map_s2[first_char]:
                char_map_s2[first_char] -= 1
                if char_map_s2[first_char] < 1:
                    del char_map_s2[first_char]
                left += 1
                if left >= len(s2):
                    break
                first_char = s2[left]

            # step 3: analyze window size, and maintain min_res.
            window_size = j+1-(left+1) + 1
            if matches == len(s1):
                if min_res_length > window_size:
                    min_res_length = window_size
                    min_res = s2[left:j+1]
            
        return min_res

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        needstr = collections.defaultdict(int)
        for ch in t:
            needstr[ch] += 1
        needcnt = len(t)
        res = (0, float('inf'))
        start = 0
        for end, ch in enumerate(s):
            if needstr[ch] > 0:
                needcnt -= 1
            needstr[ch] -= 1
            if needcnt == 0:
                while True:
                    tmp = s[start]
                    if needstr[tmp] == 0:
                        break
                    needstr[tmp] += 1
                    start += 1
                if end - start < res[1] - res[0]:
                    res = (start, end)
                needstr[s[start]] += 1
                needcnt += 1
                start += 1
        return '' if res[1] > len(s) else s[res[0]:res[1]+1]