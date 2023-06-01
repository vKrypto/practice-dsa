# https://leetcode.com/problems/longest-repeating-character-replacement/description/

from collections import Counter, defaultdict

class Solution:
    # time: o(n^3), space: o(1)
    def characterReplacement_brute_force(self, s: str, k: int) -> int:
        res = k+1
        for i in range(len(s)):
            for j in range(1,len(s)-i+1):
                temp = s[i:i+j]
                # skip loop
                if len(temp) <= res:
                    continue

                max_freq_char = max(temp, key=temp.count)
                max_freq = 0
                for l in temp:
                    if l == max_freq_char:
                        max_freq += 1

                total_un_common_digit = len(temp) - max_freq
                if total_un_common_digit <=k:
                    res = max(res, len(temp))
        return min(res, len(s))

    # time o(n^2), space: o(n)
    def characterReplacement_counter(self, s: str, k: int) -> int:
        res = k+1
        left, right = 0, k
        while left <= right and right < len(s)-1:
            right += 1
            # string from start from [i to j]
            len_temp = right-left + 1
            # find max freq char, and count
            max_item_freq = Counter(s[left:right+1]).most_common()[0][1]
            total_un_common_digit = len_temp - max_item_freq
            if total_un_common_digit <=k:
                # update max count result
                res = max(res, len_temp)
            else:
                # advance left pointer by 1
                left += 1
        return res


    # time o(n^2), space: o(n)
    def characterReplacement_two_pointer(self, s: str, k: int) -> int:
        res = k+1
        left, right = 0, k
        while left <= right and right < len(s):
            right += 1
            # string from start from [i to j]
            temp = s[left:right+1]
            # find max freq char, and count
            max_freq_char = max(temp, key=temp.count)
            max_freq = 0
            for l in temp:
                if l == max_freq_char:
                    max_freq += 1

            total_un_common_digit = len(temp) - max_freq

            if total_un_common_digit <=k:
                # update max count result
                res = max(res, len(temp))
            else:
                # advance left pointer by 1
                left += 1
        return min(res, len(s))


    # time o(26*n), space: o(n)
    def characterReplacement_two_pointer_optimized(self, s: str, k: int) -> int:
        res = k+1
        left, right = 0, 0
        
        # create a char map
        char_map = {s[0]:1}
        max_freq = 0
        while left <= right and right < len(s)-1:
            right += 1
            # update new char into map
            char_map[s[right]] = char_map.get(s[right], 0) + 1
            # len of current window
            len_temp = right-left + 1
            # find max freq item in char_map
            max_freq = char_map[max(char_map, key=char_map.get)]
            total_un_common_digit = len_temp - max_freq

            if total_un_common_digit <=k:
                # update max count result
                res = max(res, len_temp)
            else:
                # advance left pointer by 1
                char_map[s[left]] -= 1
                left += 1
        return min(res, len(s))

    # time o(n), space: o(n)
    def characterReplacement_two_pointer_optimized(self, s: str, k: int) -> int:
        res = k+1
        left, right = 0, 0
        
        # create a char map
        char_map = defaultdict(int)
        char_map[s[0]] += 1
        max_freq = 0
        while left <= right and right < len(s)-1:
            right += 1
            # update new char into map
            char_map[s[right]] = char_map.get(s[right], 0) + 1
            # len of current window
            len_temp = right-left + 1
            # find max freq item in char_map
            max_freq = max(max_freq, char_map[s[right]])
            total_un_common_digit = len_temp - max_freq

            if total_un_common_digit <=k:
                # update max count result
                res = max(res, len_temp)
            else:
                # advance left pointer by 1
                char_map[s[left]] -= 1
                left += 1
        return min(res, len(s))

    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        kk = k
        i = max_count = 0
        counts = defaultdict(int)
        for char in s:
            counts[char] += 1
            if counts[char] > max_count:
                max_count = counts[char]
            else:
                kk -= 1
            if kk < 0:
                counts[s[i]] -= 1
                i += 1
                kk += 1
        return max_count + k - kk