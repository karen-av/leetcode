"""
You are given a large integer represented as an integer array digits, where 
each digits[i] is the ith digit of the integer. The digits are ordered from 
most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.


Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""

def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    s = ''
    for i in digits:
       s+=str(i)
    x = int(s) + 1
    res = []
    for i in range(len(str(x))):
        res.append(int(str(x)[i]))
    return(res)

def plusOne_1(digits):
    
    for i in reversed(range(len(digits))):
        print(digits[i])
        if digits[i] + 1 <= 9:
            digits[i] += 1
            break
        digits[i] = 0

    if digits[0] == 0:
        digits.insert(0, 1)

    return digits 


digits = [8, 9, 9, 9]
print(plusOne_1(digits))
#assert(plusOne_1(digits)) == [9,0,0,0]
