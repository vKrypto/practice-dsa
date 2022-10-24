# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
import re
from collections import Counter

class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        invalid solution
        """
        count_map = Counter(s)
        for k, v in count_map.items():
            if v > 2:
                s = s.replace(k*2, "")
        return s
    
    def removeDuplicates_2(self, s: str) -> str:
        """
        invalid solution
        """
        dup_chars = re.findall(r'(.+)(?=.*?\1)', s)
        for dup_char in dup_chars:
            s = s.replace(dup_char*2, "")
        return s
        
    def removeDuplicates_1(self, s: str) -> str:
        """
        Runtime: 144 ms, faster than 65.13% of Python3 online submissions for Remove All Adjacent Duplicates In String.
        Memory Usage: 14.8 MB, less than 86.25% of Python3 online submissions for Remove All Adjacent Duplicates In String.
        """
        st = []
        for c in s:
            if st and st[-1] == c:
                st.pop()
            else:
                st.append(c)
        return "".join(st)
    
    def removeDuplicates_0(self, s: str) -> str:
        """
        time: o(n)
        sapce: o(1)
        using string is costly as it is immutable.
        Runtime: 662 ms, faster than 6.02% of Python3 online submissions for Remove All Adjacent Duplicates In String.
        Memory Usage: 14.9 MB, less than 51.84% of Python3 online submissions for Remove All Adjacent Duplicates In String.
        """
        temp = s[0]
        index = 1
        len_s = len(s)
        res = temp
        while index < len_s:
            if s[index]== temp:
                res  = res[:-1]
            else:
                res += s[index]
            temp = res[-1] if res else ""
            index += 1
        return res