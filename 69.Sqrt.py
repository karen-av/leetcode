"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

"""

def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    int_list = []
    length = 46350 if x > 46350 else x
    for i in range(length):
        int_list.append(i)
    def serch(int_list, x):
        if x == int_list[len(int_list) // 2] ** 2:
            return int_list[len(int_list) // 2]
        elif len(int_list) == 1:
            return int_list[0]       
        elif x > int_list[len(int_list) // 2] ** 2:
           return serch(int_list[len(int_list) // 2:], x)
        elif x < int_list[len(int_list) // 2] ** 2:
            return serch(int_list[:len(int_list) // 2], x)
    return serch(int_list, x)
                     

x = 15
# 9
# 123456789
print(mySqrt(x))
#print(x**-0.5)

