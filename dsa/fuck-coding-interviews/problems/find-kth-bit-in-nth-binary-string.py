# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/


class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        prev = "0"
        for row in range(1, n):
            invert_str = ""
            for j in prev[::-1]:
                invert_str += "1" if j == "0" else "0"

            prev = prev + "1" + invert_str

        return prev[k-1]