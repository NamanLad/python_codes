# aim is to multiply q and m

q = ['1', '1', '0', '1']
m = ['0', '1', '1', '1']

# q = list(input('Enter q'))
# m = list(input('Enter m'))


def add(a, b):
    carry = 0

    for i in range(length-1, -1, -1):
        num1 = int(a[i])
        num2 = int(b[i])
        sum = num1+num2+carry
        if sum == 0 or sum == 1:
            carry = 0
            char = str(sum)
        elif sum == 2 or sum == 3:
            carry = 1
            char = str(sum-2)

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


length = len(m)
a = list()
for _ in range(length):
    a.append('0')

q_1 = 0
charQ = '0'

for _ in range(length):
    bit = q[-1]
    string = bit + charQ
    if string == '10':
        a = add(a, compl)

    elif string == '01':
        a = add(a, m)

    # elif string == '11' or string == '00':

    charQ = q[-1]
    q = [a[3]] + q[:3]
    a = [a[0]] + a[:3]

print('ans is:')
for i in a:
    print(i, end="")
for i in q:
    print(i, end="")

