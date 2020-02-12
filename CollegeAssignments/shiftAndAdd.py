# aim is to multiply q and m

q = list(input('Enter q'))
m = list(input('Enter m'))

length = len(m)
a = list()
for _ in range(length):
    a.append('0')

carry = 0
c = '0'

for _ in range(length):
    bit = q[-1]

    if bit == '1':
        for i in range(length-1, -1, -1):
            num1 = int(a[i])
            num2 = int(m[i])
            addition = num1 + num2 + carry

            if addition == 0 or addition == 1:
                carry = 0
                c = '0'
                char = str(addition)
            elif addition == 2 or addition == 3:
                carry = 1
                c = '1'
                char = str(addition-2)
            a[i] = char

    q = [a[3]] + q[:3]
    a = [c] + a[:3]

print('ans is:')
print(c, end="")
for i in a:
    print(i, end="")
for i in q:
    print(i, end="")

