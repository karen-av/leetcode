'''
Given an array of integers nums and an integer target, return indices of 
the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Учитывая массив целых чисел nums и целое число target, верните индексы 
двух чисел, таких, что их сумма равна target.

Вы можете предположить, что каждый вход будет иметь ровно одно решение, 
и вы не можете использовать один и тот же элемент дважды.

Вы можете вернуть ответ в любом порядке.
'''


def twoSum(nums, target):
    for i in range(len(nums) - 1):
        k = 1
        while k < len(nums) - i:
            print(nums[i], nums[i+k])
            if nums[i] + nums[i+k] == target:
                return [i, i+k]
            k+=1  
            

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


nums = [-1,-2,-3,-4,-5]
#nums = [3,3]
target = -8
Output= [0,1]
print(twoSum(nums, target))
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].