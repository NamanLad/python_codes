# unsigned division
# aim is to divide q by m

m = list(input('Enter m'))
q = list(input('Enter q'))

q0 = q[-1]


def add(a, b):
    carry = 0

    for i in range(length - 1, -1, -1):
        num1 = int(a[i])
        num2 = int(b[i])
        sum = num1 + num2 + carry
        if sum == 0 or sum == 1:
            carry = 0
            char = str(sum)
        elif sum == 2 or sum == 3:
            carry = 1
            char = str(sum - 2)

        a[i] = char

    return a


def compliment(arr):
    complArr = list()
    for i in arr:
        if i == '1':
            complArr.append('0')
        else:
            complArr.append('1')

    if complArr[-1] == '0':
        complArr[-1] = '1'

    else:
        i = length - 1
        while i > 0 and complArr[i] == '1':
            complArr[i] = '0'
            i -= 1

        if i != 0:
            complArr[i] = '1'

    return complArr


length = len(m)
compl = list()
compl = compliment(m)

a = list()
for _ in range(length):
    a.append('0')

for _ in range(length - 1):
    a = a[1:] + [q[0]]
    q = q[1:] + ['-']
    q0 = '-'

    if a[0] == '1':
        a = add(a, m)
    else:
        a = add(a, compl)

    if a[0] == '1':
        q0 = '0'
    else:
        q0 = '1'
    q[-1] = q0

if a[0] == '1':
    a = add(a, m)

print('quotient is: ', end="")
for i in q:
    print(i, end="")

print('\nremainder is: ', end="")
for i in a:
    print(i, end="")

