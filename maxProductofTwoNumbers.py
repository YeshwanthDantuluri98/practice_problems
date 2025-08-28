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
max_product(arr)


# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
#
# myList = [1, 2, 3, 4]
# middle(myList)  # [2,3]

def middleList(lst):
    return lst[1:-1]

myList = [1,2,3,4]
print(middleList(myList))

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
print(diagonal_sum(matrix_2d))
