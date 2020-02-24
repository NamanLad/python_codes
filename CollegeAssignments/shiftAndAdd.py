# aim is to multiply q and m


"""
using full adder logic
for adding a, b, c
sum = a XOR b XOR c
carry = ab + c*(a XOR b)
"""


def add(a, m):
    c = 0
    for i in range(length-1, -1, -1):
        num1 = int(a[i])
        num2 = int(m[i])

        sum = num1 ^ num2 ^ c
        carry = num1 & num2 | (c & (num1 ^ num2))
        a[i] = str(sum)
        c = carry
    return str(c)


def display(c, a, q):

    # print('ans is:')
    print()
    print(c, end=" ")
    for i in a:
        print(i, end="")
    print(end=" ")
    for i in q:
        print(i, end="")


def right_shift(c, a, q):

    q = [a[-1]] + q[:-1]
    a = [c] + a[:-1]
    c = '0'

    return c, a, q


q = list(input('Enter q'))
m = list(input('Enter m'))

length = len(m)
a = list()
for _ in range(length):
    a.append('0')

c = '0'

for _ in range(length):
    display(c, a, q)
    bit = q[-1]

    if bit == '1':
        c = add(a, m)

    c, a, q, = right_shift(c, a, q)

display(c, a, q)




