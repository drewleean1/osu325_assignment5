#Name: Andrew Lee
#OSU 325
#Assignment 5: Amount.py
#Due date: February 13, 2023

from copy import deepcopy

def combination_sum_helper(nums, start, result, remainder, combination):

    if(remainder == 0):
        combination.sort()
        if combination not in result:
            result.append(deepcopy(combination))
        return
    elif( remainder <0):
        return # sum exceeded the target
    for i in range(start, len(nums)):
        combination.append(nums[i])
        combination_sum_helper(nums, i+1, result, remainder-nums[i], combination)
        #backtrack
        combination.pop()


def amount(nums, target):
    result = []
    combination_sum_helper(nums,0, result, target,[])
    return result

