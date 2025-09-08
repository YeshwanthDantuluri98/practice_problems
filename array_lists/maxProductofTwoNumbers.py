# Find the maximum product of two integers in an array where all elements are positive.
#
# Example
#
# arr = [1, 7, 3, 4, 9, 5]
# max_product(arr) # Output: 63 (9*7)

def max_product(arr):
    final_array = []
    for i in range(len(arr)):
        num1 = arr[i]
        for j in range(len(arr)):
            if i != j:
                num2 = arr[j]
                final_array.append(num1 * num2)

    print(max(final_array))
    return (max(final_array))

arr = [1,7,3,4,9,5]
# max_product(arr)


# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
#
# myList = [1, 2, 3, 4]
# middle(myList)  # [2,3]

def middleList(lst):
    return lst[1:-1]

myList = [1,2,3,4]
# print(middleList(myList))

# Given 2D list calculate the sum of diagonal elements.
# Example
# myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# diagonal_sum(myList2D)  # 15
def diagonal_sum(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]

    return total
    # TODO


matrix_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(diagonal_sum(matrix_2d))

# Given a list, write a function to get first, second best scores from the list.
# List may contain duplicates.
# Example
# myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
# first_second(myList) # 90 87

def first_second(my_list):
    major_number = max(my_list)
    my_list.remove(major_number)
    second_major_number = max(my_list)
    # print(second_major_number)
    return major_number, second_major_number
    # return my_list

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
# print(first_second(myList))

def remove_diplicates(arr):
    pure_list = list(set(arr))
    return pure_list

danger_arr = [1,1,2,2,3,4,4,5]
# print(remove_diplicates(danger_arr))


#method -1
def contains_duplicates(nums_arr):
    seen = set()
    for num in nums_arr:
        if num in seen:
            return True
        seen.add(num)

    return False

# print(contains_duplicates([1,2,3,1]))

#method -2
def contains_duplicates2(nums_arr):
    new_arr = list(set(nums_arr))
    send_value = False
    if len(nums_arr) != len(new_arr):
        send_value = True

    return send_value

# print(contains_duplicates2([1,2,3,1,3]))

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    else:
        return False

list1 = [2,1,3]
list2 = [1,3,2]
permutation(list1, list2)