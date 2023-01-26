"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.
"""

#
def isPalindrome(x):

    return True if str(x) == str(x)[::-1] else False


x = 123
y = int(str(x)[::-1])
print(y)
print(isPalindrome(x))
