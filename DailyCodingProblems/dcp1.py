"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

array = [10, 15, 3, 7]
k = 17

residueArray = list()

for i in range(len(array)):
    residueArray.append(k - array[i])
    if i != 0:
        for val in residueArray:
            if array[i] == val:
                print("Pair found!")
                exit()
else:
    print("No pair found")




