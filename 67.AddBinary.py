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

    res = ''
    x = int(a) + int(b)
    if x == 0:
        return '0'
    tmp = 0
    for i in reversed(str(x)):
        if int(i) + tmp != 2:
            res = '1' + res
            tmp = 0
        else:
            res = '0' + res
            tmp = 1

    if tmp == 1:
        res = '1' + res
    return res


a = '1010'
b = '1011'
print(addBinary(a,b))
