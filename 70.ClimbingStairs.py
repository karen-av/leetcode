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

"""

def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """

  
    return  1 if n <= 1 else climbStairs(n - 1) + climbStairs(n - 2) 


"""
 sl = set()
    digit = ''.join(['1' for i in range(n)]) # 111111 21111 2211 222
    for i in range(n//2 + 1):
        print(digit)
        for p in range(len(digit)):
            print(p)
        digit = digit[2:] + '2'"""
#for p in itertools.permutations(digit):
    #sl.add(''.join(p))

   

x = 45
print(climbStairs(x))
#assert(climbStairs(4)) == 5, 4
#assert(climbStairs(5)) == 8, 5
#assert(climbStairs(7)) == 21, 7