# https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    
    def kthGrammar_recursive(self, n: int, k: int) -> int:
        def row_data(row_index):
            if row_index == 0:
                return '0'
            prev_row = row_data(row_index-1)
            res = ""
            for i in prev_row:
                res += "01" if i == '0' else "10"
            return res

        row_n = row_data(n) 
        return int(row_n[k-1])
    
    def kthGrammar_iterative(self, n: int, k: int) -> int:
        
        prev_row = "0"
        
        for row_index in range(1, n):
            if row_index == 0:
                return '0'
            res = ""
            for i in prev_row:
                res += "01" if i == '0' else "10"
            prev_row = res

        return int(prev_row[k-1])

    def kthGrammar_optimized(self, n: int, k: int) -> int:
        def row_data(row_index, col_index):
            if row_index == 0:
                return '0'
            
            prev_row = row_data(row_index-1, col_index//2)
            res = "01" if prev_row == '0' else "10"
            return res[col_index % 2]

        return int(row_data(n-1, k-1) )
    
"""   
01
0110
01101001
0110100110010110
01101001100101101001011001101001
0110100110010110100101100110100110010110011010010110100110010110
01101001100101101001011001101001100101100110100101101001100101101001011001101001011010011001011001101001100101101001011001101001
"""