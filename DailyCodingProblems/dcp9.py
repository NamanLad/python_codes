"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10,
since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

array = [2, 4, 6, 2, 5]
# ans = 13 (2, 6, 5)

# array = [5, 1, 1, 5]
# ans is 10 (5, 5)


sumForEvenIndex = 0
sumForOddIndex = 0
mySum = 0

for i in range(len(array)):

    if i == 0:
        sumForEvenIndex = array[0]
    elif i == 1:

        if array[1] > array[0]:
            sumForOddIndex = array[1]
        else:
            sumForOddIndex = array[0]

    elif i % 2 == 0:
        if sumForEvenIndex + array[i] >= sumForOddIndex or array[i] > sumForOddIndex:
            sumForEvenIndex += array[i]
        else:
            sumForEvenIndex = sumForOddIndex

    elif i % 2 == 1:
        if sumForOddIndex + array[i] >= sumForEvenIndex or array[i] > sumForEvenIndex:
            sumForOddIndex += array[i]
        else:
            sumForOddIndex = sumForEvenIndex


if sumForOddIndex > sumForEvenIndex:
    mySum = sumForOddIndex
else:
    mySum = sumForEvenIndex

print(mySum)


