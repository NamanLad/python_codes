"""
Write a function that rotates a list by k elements. For example,
[1, 2, 3, 4, 5, 6] rotated by two becomes
[3, 4, 5, 6, 1, 2]. Try solving this without creating a copy of the list.
How many swap or move operations do you need?
"""

noOfElements = 6  # n
noOfShifts = 2  # k

question = [1, 2, 3, 4, 5, 6]

# right shift...
# ans should be [6, 7, 1, 2, 3, 4, 5]


def myFunction(array, n, k):

    if n % k == 0:
        # print("Divisible...")

        noOfRounds = k
        for i in range(noOfRounds):

            temp = array[i]
            for j in range(int(n / k)):

                oldValue = array[-(((j+1)*k - i) % n)]
                array[-(((j+1)*k - i) % n)] = temp
                temp = oldValue

    else:

        temp = array[0]
        for i in range(n):

            # switch (i)th val and (i+k)th val, after storing (i+k)th val as OldValue.....
            oldValue = array[-(((i+1)*k) % n)]
            array[-(((i+1)*k) % n)] = temp
            temp = oldValue

    print(array)


myFunction(question, noOfElements, noOfShifts)




