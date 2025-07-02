"""
Write a function to find the missing number in a given integer array of 1 to 100.
The function takes to parameter the array and the number of elements that needs to be in array.
For example if we want to find missing number from 1 to 6 the second parameter will be 6.

For Example missing_number([1,2,3,4,6],6) Answer would be 5
"""

def missing_number(arr,n):
    temp = []
    for i in range(n):
        temp.append(i+1)
    missing_number = list(set(temp) - set(arr))
    return missing_number[0]


missing_number([1,2,3,4,6],6)

def missing_number_2(arr, n):
    total = n * (n+1) // 2
    sum_arr = sum(arr)
    missing_number = total - sum_arr
    return missing_number

missing_number_2([1,2,3,4,5],6)