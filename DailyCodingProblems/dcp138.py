"""
Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
"""

n = 101
# my denominations are: 1, 5, 10, 25

noOf25 = 0
noOf10 = 0
noOf5 = 0
noOf1 = 0

temp = n

if temp >= 25:
    noOf25 = int(temp / 25)
    remainder25 = temp - (noOf25 * 25)
    temp = remainder25


if temp >= 10:
    noOf10 = int(temp / 10)
    remainder10 = temp - (noOf10 * 10)
    temp = remainder10


if temp >= 5:
    noOf5 = int(temp / 5)
    remainder5 = temp - (noOf5 * 5)
    temp = remainder5


if temp >= 1:
    noOf1 = int(temp / 1)
    remainder1 = temp - (noOf1 * 1)
    temp = remainder1


print('no of 25: ', noOf25)
print('no of 10: ', noOf10)
print('no of 5: ', noOf5)
print('no of 1: ', noOf1)
