

"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.


"""

class RomanNumerals:
    
    

    def from_roman(s):
        number = 0
        
        i = 0
        roman = s
        while len(roman) > i and roman[i] == 'M':
            number += 1000
            i += 1
        roman = roman[i:]
        
        i = 0
        while len(roman) > i and (roman[i] == 'C' or roman[i] == 'D' or roman[i] == 'M'):
            if roman[i] == 'C':
                number += 100
                i += 1
            elif roman[i] == 'D':
                if i == 0:
                    number += 500
                elif i == 1:
                    number += 300
                i += 1
            elif roman[i] == 'M':
                number += 800
                i += 1
        roman = roman[i:]

        i = 0
        while len(roman) > i and (roman[i] == 'X' or roman[i] == 'L' or roman[i] == 'C'):
            if roman[i] == 'X':
                number += 10
                i += 1
            elif roman[i] == 'L':
                if i == 0:
                    number += 50
                elif i == 1:
                    number += 30
                i += 1
            elif roman[i] == 'C':
                number += 80
                i += 1
        roman = roman[i:]
        
        i = 0
        while len(roman) > i and (roman[i] == 'I' or roman[i] == 'V' or roman[i] == 'X'):
            if roman[i] == 'I':
                number += 1
                i += 1
            elif roman[i] == 'V':
                if i == 0:
                    number += 5
                elif i == 1:
                    number += 3
                i +=1
            elif roman[i] == 'X':
                number += 8
                i += 1

        return number


x = 1243
y = 'MCDXLIII'
print(f'x = {RomanNumerals.to_roman(x)}')
print(f'y = {RomanNumerals.from_roman(y)}')