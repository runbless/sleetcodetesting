'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII,
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
 he same principle applies to the number nine, which is written as IX.

There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9.
IV = 4 / IX = 9

X can be placed before L (50) and C (100) to make 40 and 90.
XL = 40 / XC = 90

C can be placed before D (500) and M (1000) to make 400 and 900.
CD = 400 / CM = 900

Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
'''


class Solution:
    def strToint(self, key) -> int:
        matching = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }.get(key, "Error")
        return matching

    def StrToList(self, s: str) -> list:
        '''
        스트링을 각 단어단위로 쪼개서 리스트로 담고,
        특정 조건에 해당하면 해당조건은 붙여서 담는다.
        조건 : C, X, I 문자열 뒤에 동일한게 붙는지 체크하고,
        동일한게 붙지않으면 연결내용으로 넘겨보기.
        '''
        chars = list(s)
        str_filter = ["I", "X", "C"]

        chklist = []
        dummy = ""
        for c in chars:
            if dummy == "":
                if not c in str_filter:
                    chklist.append(c)
                else:
                    dummy += c
            else:
                if type(self.strToint(dummy+c)) is int:
                    dummy += c
                else:
                    chklist.append(dummy)
                    dummy = ""
                    dummy += c

            if len(dummy) == 2:
                chklist.append(dummy)
                dummy = ""

        if not dummy == "":
            chklist.append(dummy)

        return chklist

    def romanToInt(self, s: str) -> int:
        result = 0
        summit = self.StrToList(s)
        for i in summit:
            result += self.strToint(str(i))

        return result

s = "MCMXCIV"
print(Solution().romanToInt(s))

'''
Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

