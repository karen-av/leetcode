"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

:type n: int
:rtype: int
"""

def climbStairs_0(n):
     return  1 if n <= 1 else climbStairs_0(n - 1) + climbStairs_0(n - 2) 

def climbStairs_1(n):
    if n <= 3:
        return n
    x = 3
    y = 2
    while(n > 3):
        x = x + y
        y = x - y
        n -= 1
    return x 

def climbStairs_2(n):
    if n <= 3:
        return n
    x = 3
    y = 2
    for i in range(3, n):
        x = x + y
        y = x - y
    return x

x = 45
print(climbStairs_0(x))
assert(climbStairs_0(4)) == 5, 4
assert(climbStairs_1(5)) == 8, 5
assert(climbStairs_2(7)) == 21, 7