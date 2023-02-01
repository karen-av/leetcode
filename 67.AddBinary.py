"""
Given two binary strings a and b, return their sum as a binary string.

Input: a = "11", b = "1"
Output: "100"

Input: a = "1010", b = "1011"
Output: "10101"

"""


def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    #2222
    res = ''
    x = int(a) + int(b)
    if x == 0:
        return '0'
    tmp = 0
    print(x)
    for i in reversed(str(x)):
        #print(int(i) + tmp)
        if int(i) + tmp < 2 and int(i) + tmp != 0:
            res = '1' + res
            tmp = 0
        elif int(i) + tmp > 2:
            res = '1' + res
        elif int(i) + tmp == 2:
            res = '0' + res
            tmp = 1
        else:
            res = '0' + res

    if tmp == 1:
        res = '1' + res
    return res


def addBinary_1(a, b):
    res = ''
    tmp = 0
    x = str(int(a) + int(b))
    while x:
        char = x[len(x) - 1:]
        res = str((int(char) + tmp) % 2) + res
        tmp = (int(char) + tmp) // 2
        x = x[:len(x) - 1]
    if int(a) + int(b) != 0 and (res[0] == '0' or tmp != 0):
        res = '1' + res
    return res



a = '1'
b = '11'
print(addBinary_1(a,b))
