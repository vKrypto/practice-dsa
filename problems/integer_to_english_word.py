# https://leetcode.com/problems/integer-to-english-words/description/

class Solution:
    number_words = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
                "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", 
                "Eighteen", "Nineteen", "Twenty"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def convert_2_digit_num_to_str(self, n):
        n = n%100
        if n <= 20:
            return self.number_words[n]
        else:
            res = [self.tens[n//10]]
            if n%10:
                res.append(self.number_words[n%10])
            return " ".join(res)

    def convert_3_digit_num_to_str(self, n):
        # [0, 999]
        res = []
        k, n  = n // 10**2, n% 10**2
        
        if k:
            res.append(f"{self.number_words[k]} Hundred")
        if n:
            if n < 20:
                res.append(self.number_words[n])
            else:
                res.append(self.convert_2_digit_num_to_str(n))
        return " ".join(res)

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        levels = [
            "", "Thousand", "Million", "Billion", "Trillion"
        ]
        res = []
        temp = num
        while temp:
            res.append(temp % (10**3))
            temp = temp // 10**3
        temp = []
        for i, num in enumerate(res):
            if not num:
                continue
            if i > 0:
                temp.append(f"{self.convert_3_digit_num_to_str(num)} {levels[i]}")
            else:
                temp.append(f"{self.convert_3_digit_num_to_str(num)}")
        return " ".join(temp[::-1])



class Solution2:
    MAP = {
        0: '',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen',
        20: 'Twenty',
        30: 'Thirty',
        40: 'Forty',
        50: 'Fifty',
        60: 'Sixty',
        70: 'Seventy',
        80: 'Eighty',
        90: 'Ninety',
        100: 'Hundred',
        1000: 'Thousand',
        1e6: 'Million',
        1e9: 'Billion'
    }

    # using recursion
    def numberToWords(self, num: int) -> str:
        def helper(num):
            if num < 21:
                return self.MAP[num]
            if num < 100:
                mod = num % 10
                return f'{self.MAP[num - mod]} {helper(mod)}'.strip()
            for base in [1e9, 1e6, 1000, 100]:
                if num >= base:
                    return f'{helper(num // base)} {self.MAP[base]} {helper(num % base)}'.strip()
            return ''

        return 'Zero' if not num else helper(num)