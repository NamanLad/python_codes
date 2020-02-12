"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""
def fibonacci(n):
    if n == 1 or n == 2:
        return n

    else:
        return fibonacci(n-1) + fibonacci(n-2)


number = int(input("Enter the number to be decoded"))
strNumber = str(number)
strings = list()
startIndex = 0

for i in range(0, len(strNumber)):
    if int(strNumber[i]) != 1 and int(strNumber[i]) != 2:
        endIndex = i+1
        currentString = strNumber[startIndex:endIndex]
        strings.append(currentString)
        startIndex = endIndex

    elif i == len(strNumber)-1:
        endIndex = i+1
        strings.append(strNumber[startIndex:endIndex])

ans = 1


for i in strings:
    if len(i) == 1:
        ans *= 1
    else:
        if '3' <= i[-1] <= '6':
            ans *= fibonacci(len(i))

        else:
            if i[-2] == '1':
                ans *= fibonacci(len(i))
            else:
                ans *= fibonacci(len(i) - 1)


print(ans)
