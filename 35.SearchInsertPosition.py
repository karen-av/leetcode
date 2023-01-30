"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the index 
where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    index = 0
    while nums:
        print(f'len - {len(nums) // 2}, item -  {nums[len(nums) // 2]}, nums -  {nums}')
        if target > nums[len(nums) // 2]:
            index += len(nums) // 2 + 1
            del nums[0:len(nums) // 2 + 1]
        elif target < nums[len(nums) // 2]:
            del nums[len(nums) // 2:]
        elif target == nums[len(nums) // 2]:
            return index + len(nums) // 2
    return index 

 


nums = [1, 3, 5, 8, 10]
target = 11
print(searchInsert(nums, target))