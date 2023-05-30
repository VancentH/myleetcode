"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Time complexity: O(n)
Space complexity: O(n)
"""

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    num_dict  = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict: # check value in dictionary
            return [num_dict[complement], i]
        num_dict[num] = i # store {value1: index1, value2: index2, ...}
    
print(twoSum([3,2,4], 6))

