"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

"""

def sumOfTwoNumbers(array,total):
    check_num = {}
    for i, num in enumerate(array):
        diff = total - num
        if diff in check_num:
            return [check_num[diff], i]
        check_num[num] = i


# print(sumOfTwoNumbers([2,6,3,9,11],9))

def pair_sum(myList, sum):
    pair_list = []
    seen = set()

    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] + myList[j] == sum and (myList[i], myList[j]) not in seen:
                pair_list.append(f'{myList[i]}+{myList[j]}')
                seen.add((myList[i],myList[j]))

    return pair_list



# print(pair_sum([2,4,3,5,6,-2,4,7,8,9],7))