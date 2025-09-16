# Creating a new tuple
newtuple1 = tuple('abcde')
# print(newtuple1)

#Accessing Tuple
# print(newtuple1[::2])
for i in range(len(newtuple1)):
    print(newtuple1[i])

print('a' in  newtuple1)
print(newtuple1.index('a'))

init_tuple_a = 1, 2
init_tuple_b = (3, 4)

# [print(sum(x)) for x in [init_tuple_a + init_tuple_b]]

#Problem -1
# Sum and Product
# Write a function that calculates the sum and product of all elements in a tuple of numbers.
#
# Example
# input_tuple = (1, 2, 3, 4)
# sum_result, product_result = sum_product(input_tuple)
# print(sum_result, product_result)  # Expected output: 10, 24

def sum_product(input_tuple):
    print("Test")
    sum_result = 0
    product_result = 1
    for i in range(len(input_tuple)):
        sum_result += input_tuple[i]
        product_result *= input_tuple[i]
    return sum_result,product_result


# print(sum_product((1,2,3,4)))

# Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.
#
# Example
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# output_tuple = tuple_elementwise_sum(tuple1, tuple2)
# print(output_tuple)
# Expected output: (5, 7, 9)
#method -1
def tuple_elementwise_sum(tuple1, tuple2):
    return tuple(map(sum,zip(tuple1, tuple2)))

# print(tuple_elementwise_sum((1,2,3), (4,5,6)))

#method -2
def tuple_elementwise_sum2(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        return "Not Happening"

    result = tuple(a+b for a,b in zip(tuple1, tuple2))
    return result

# print(tuple_elementwise_sum2((1,2,3),(4,5,6)))

# Insert at the Beginning
# Write a function that takes a tuple and a value, and returns a new tuple with the value inserted at the beginning of the original tuple.
#
# Example
#
# input_tuple = (2, 3, 4)
# value_to_insert = 1
# output_tuple = insert_value_front(input_tuple, value_to_insert)
# print(output_tuple)

#method -1
def insert_value_front(input_tuple, value_to_insert):
    val_tup = list(input_tuple)
    val_tup.insert(0,value_to_insert)
    t = tuple(val_tup)
    return t

print(insert_value_front((2,3,4),1))

#method -2
def insert_value_at_beginning(input_tuple, value_to_insert):
    return (value_to_insert,) + input_tuple

print(insert_value_at_beginning((2,3,4),1))

# Write a function that takes a tuple of strings and concatenates them, separating each string with a space.
#
# Example
# input_tuple = ('Hello', 'World', 'from', 'Python')
# output_string = concatenate_strings(input_tuple)
# print(output_string)  # Expected output: 'Hello World from Python'

def concatenate_strings(input_tuple):
    return " ".join(input_tuple)

print(concatenate_strings(('Hello', 'World', 'from', 'Python')))


# Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.
#
# Example
# input_tuple = (
#     (1, 2, 3),
#     (4, 5, 6),
#     (7, 8, 9)
# )
# output_tuple = get_diagonal(input_tuple)
# print(output_tuple)  # Expected output: (1, 5, 9)

def get_diagonal(tup):
    return tuple(tup[i][i] for i in range(len(tup)))

print(get_diagonal(( (1, 2, 3),(4, 5, 6),(7, 8, 9))))

# Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.
#
# Example
# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (4, 5, 6, 7, 8)
# output_tuple = common_elements(tuple1, tuple2)
# print(output_tuple)  # Expected output: (4, 5)

def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))

print(common_elements((1,2,3,4,5),(4,5,6,7,8)))
