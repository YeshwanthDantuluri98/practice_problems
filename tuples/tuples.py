# Creating a new tuple
newtuple1 = tuple('abcde')
print(newtuple1)

#Accessing Tuple
# print(newtuple1[::2])
for i in range(len(newtuple1)):
    print(newtuple1[i])

print('a' in  newtuple1)
print(newtuple1.index('a'))

init_tuple_a = 1, 2
init_tuple_b = (3, 4)

[print(sum(x)) for x in [init_tuple_a + init_tuple_b]]

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


print(sum_product((1,2,3,4)))