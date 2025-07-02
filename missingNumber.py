def missing_number(arr,n):
    temp = []
    for i in range(n):
        temp.append(i+1)
    print(temp)
    getMissingNumber = list(set(temp) - set(arr))
    return getMissingNumber[0]


missing_number([1,2,3,4,6],6)

def missing_number_2(arr, n):
    total = n * (n+1) // 2
    sum_arr = sum(arr)
    missing_number = total - sum_arr
    print(missing_number)

missing_number_2([1,2,3,4,5],6)