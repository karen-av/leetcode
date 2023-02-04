"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given 
number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

:type s: str
:type numRows: int
:rtype: str
"""

def convert(s, numRows):
    rs = [[] for i in range(numRows)]
    w, i  = 0, 0
    while w < len(s):
        if i == 0: # Рисуем вниз
            while i < numRows and w < len(s):
                rs[i].append(s[w])
                w += 1
                i += 1
        else: # Рисуем вверх
            i -= 1
            while i > 1 and w < len(s):
                i -= 1
                rs[i].append(s[w])
                w += 1
                
    return ''.join([''.join(i) for i in rs])



s = "PAYPALISHIRING"
numRows = 4
#"PINALSIGYAHRPI"
res = convert(s, numRows)

print(res)
assert(convert(s, numRows)) == "PINALSIGYAHRPI"
assert(convert("A", 1)) == "A"
assert(convert("PAYPALISHIRING", 3)) == "PAHNAPLSIIGYIR"

"""
rs = ''
    a = []
    i, k  = 0, 0
    while k < len(s) - 8:
        a.append(s[k])
        print(f'k - {k}')
        while k + i + (numRows * 2 - 2) <= len(s) - 1:
            a.append(s[k + i + (numRows * 2 - 2)])
            print(k + i + (numRows * 2 - 2))
            i += 6

        i = 0
        k += 1"""