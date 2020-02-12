"""
Given a number represented by a list of digits, find the next greater permutation of a number, in terms of
lexicographic ordering. If there is not greater permutation possible, return the permutation with the lowest
value/ordering.

For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should return [2,1,3].
The list [3,2,1] should return [1,2,3].

Can you perform the operation without allocating extra memory (disregarding the input memory)?
"""

question0 = [5, 1, 3, 4, 2]
# ans should be [5, 1, 4, 2, 3]

# let length = n
# let value be at k th position from end


def sort(first, last):
    for i in range(first, last):
        for j in range(first, last-1):
            if question0[j] > question0[j+1]:
                temporary = question0[j]
                question0[j] = question0[j+1]
                question0[j+1] = temporary


i = len(question0) - 1

if question0[i] > question0[i-1]:
    temp = question0[i]
    question0[i] = question0[i-1]
    question0[i-1] = temp

else:
    while question0[i] <= question0[i-1] and i > 0:  # O(k)
        i -= 1

    if i == 0:
        sort(0, len(question0))   # O(nlogn) (best)     O(n*n) (worst)   --that's ok

    else:
        value = question0[i-1]
        valueIndex = i-1
        currentHighest = question0[i]
        currentHighestIndex = i

        while i < len(question0):   # O(k)
            if currentHighest > question0[i] > value:
                currentHighest = question0[i]
                currentHighestIndex = i
            i += 1

        temp = question0[currentHighestIndex]
        question0[currentHighestIndex] = question0[valueIndex]
        question0[valueIndex] = temp

        sort(valueIndex+1, len(question0))   # O(klogk) (best)     O(k*k) (worst)   --that's ok

print(question0)


# Total time is: O(1) (best)(k=1)     O(n*nlogn) (worst) (k = n)
