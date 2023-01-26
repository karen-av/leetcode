

"""

"""

class RomanNumerals:
    
    def to_roman(val):
        val = str(val)
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