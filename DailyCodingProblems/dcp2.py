"""
Given an array of integers, return a new array such that each element at index i of the new array is the product
of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our
input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

array = [1, 2, 3, 4, 5]

ansArray = list()
leftArray = list()
rightArray = list()


for i in range(len(array)):
    leftProduct = 1
    if i != 0:
        for j in range(i):
            leftProduct *= array[j]

    leftArray.append(leftProduct)

    rightProduct = 1
    if i != len(array)-1:
        for j in range(i+1, len(array)):
            rightProduct *= array[j]

    rightArray.append(rightProduct)

    ansArray.append(leftArray[i] * rightArray[i])


print(ansArray)

