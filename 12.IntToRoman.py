"""
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000


"""

def to_roman(num):
        val = str(num)
        res = ''

        length = len(val)
        if length == 4:
            for i in range(int(val[0])):
                res += 'M'
            val = val[1:]

        if int(val[0]) != 0 and length >= 3:
            if int(val[0]) >= 1 and int(val[0]) <= 3:
                for d in range(int(val[0])):
                    res += 'C'
            elif int(val[0]) != 0 and int(val[0]) == 4:
                res += 'CD'
            elif int(val[0]) != 0 and int(val[0]) == 5:
                res += 'D'
            elif int(val[0]) >= 6 and int(val[0]) <= 8:
                res += 'D'
                print(int(val[0]) - 5)
                for d in range(int(val[0]) - 5):
                    res += 'C'
            elif int(val[0]) >= 9:
                res += 'CM'
            val = val[1:]
        elif int(val[0]) == 0 and length >= 3:
            val = val[1:]

        if int(val[0]) != 0 and length >= 2:
            if int(val[0]) == 1:
                res += 'X'
            elif int(val[0]) >= 2 and int(val[0]) <= 3:
                for i in range(int(val[0])):
                    res += 'X'
            elif int(val[0]) == 4:
                res += 'XL'
            elif int(val[0]) == 5:
                res += 'L'
            elif int(val[0]) >= 5 and int(val[0]) <= 8:
                res += 'L'
                for i in range(int(val[0]) - 5):
                    res += 'X'
            elif int(val[0]) >= 9:
                res += 'XC'
            val = val[1:]
        elif int(val[0]) == 0 and length >= 2:
            val = val[1:]

        if int(val[0]) != 0 and length >= 1:
            if int(val[0]) >= 1 and int(val[0]) <= 3:
                for i in range(int(val[0])):
                    res += 'I'
            elif int(val[0]) == 4:
                res += "IV"
            elif int(val[0]) == 5:
                res += 'V'
            elif int(val[0]) >= 5 and int(val[0]) <= 8:
                res += "V"
                for i in range(int(val[0]) - 5):
                    res += 'I'
            elif int(val[0]) >= 9:
                res += 'IX'

        return res
            