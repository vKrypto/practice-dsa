# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
from  typing import List

class Solution:
    def check_last_k_items(self, ls:List, k:int, s: str) -> bool:
        if len(ls)< k-1:
            return False
        for i in range(k-1):
            if ls[-(i+1)] != s:
                return False
        return True

    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        for c in s:
            if st and self.check_last_k_items(st, k, c):
                # print(st)
                for _ in range(k-1):
                    st.pop()
            else:
                st.append(c)
        return "".join(st)
    
    
        