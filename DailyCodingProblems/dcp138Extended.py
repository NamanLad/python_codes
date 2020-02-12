"""
Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
"""
n = 101

denominationsArray = [25, 10, 5, 1]

countArray = list()

temp = n

for i in range(len(denominationsArray)):
    if temp < denominationsArray[i]:
        countArray.append(0)
        continue

    countArray.append(int(temp / denominationsArray[i]))
    remainder = temp - (countArray[i] * denominationsArray[i])
    temp = remainder

print(denominationsArray)
print(countArray)
mySum = 0
for count in countArray:
    mySum += count

print('No of coins reqd is ', mySum)




