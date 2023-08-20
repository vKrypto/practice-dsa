# https://leetcode.com/problems/decode-string/submissions/


class Solution:
    
    def decodeString(self, s: str) -> str:
        def decode_helper(s, i):
            result = ""
            while i < len(s):
                if s[i].isdigit():
                    num_str = ""
                    while i < len(s) and s[i].isdigit():
                        num_str += s[i]
                        i += 1
                    num = int(num_str)

                    # Find the opening bracket
                    i += 1
                    decoded_str, i = decode_helper(s, i)

                    # Find the closing bracket
                    i += 1
                    result += num * decoded_str
                elif s[i].isalpha():
                    result += s[i]
                    i += 1
                else:
                    break
            return result, i

        decoded_string, _ = decode_helper(s, 0)
        return decoded_string
