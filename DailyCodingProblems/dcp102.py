# Given a list of integers and a number K, return which contiguous elements of the list sum to K.
#
# For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
import time

question = [1, 2, 3, 4, 5]
question = list()
for i in range(10):
    question.append(i+1)

k = 54

output = list()


def function():

    for i in range(0, len(question)):
        output.append(question[i])
        ans = question[i]
        for j in range(i+1, len(question)):
            output.append(question[j])
            ans += question[j]
            if ans == k:
                print("Successful")
                print(output)
                exit()

        output.clear()

    else:
        print("Unsuccessful")
        output.clear()


function()

