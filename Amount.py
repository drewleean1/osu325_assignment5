#Name: Andrew Lee
#OSU 325
#Assignment 5: Amount.py
#Due date: February 13, 2023

from copy import deepcopy

def amount_helper(nums, start, result, remainder, combination):
    '''helper function for amount'''
    if(remainder == 0):
        if combination not in result:
            result.append(deepcopy(combination))
        return
    elif( remainder <0):
        return # sum exceeded the target
    for i in range(start, len(nums)):
        combination.append(nums[i])
        amount_helper(nums, i+1, result, remainder-nums[i], combination)
        #slight mod to Exploration code as we cannot use the same number twice.
        #backtrack
        combination.pop()


def amount(nums, target):
    '''function that takes a list of numbers (nums) and a given sum (target). Returns an array of all numbers in nums,
    without duplicates, that add up to the target. Adapted from the code in Exploration 5.2'''
    result = []
    nums.sort()                                             #nlogn time
    #sort nums before passing it through the helper function
    amount_helper(nums,0, result, target,[])
    return result

