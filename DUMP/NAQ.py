import sys

class1 = input()
class2 = input()
res = class1 + class2
reslist = sorted(res)
print(''.join(reslist))

# r = problemC()
# print(r)

import sys

num1 = input()
num2 = input()
num3 = input()

temp = int(num1) - int(num2) - int(num3)

if temp > 0:
    min1 = temp
else:
    min1 = float('inf')

temp = int(num1) - int(num2) + int(num3)

if temp > 0:
    min2 = temp
else:
    min2 = float('inf')

temp = int(num1) + int(num2) - int(num3)

if temp > 0:
    min3 = temp
else:
    min3 = float('inf')

temp = int(num1) - int(num2) / int(num3)
if temp > 0 and temp % 1 == 0:
    min4 = temp
else:
    min4 = float('inf')

temp = int(num1) / int(num2) - int(num3)
if temp > 0 and temp % 1 == 0:
    min5 = temp
else:
    min5 = float('inf')

temp = int(num1) - int(num2) - int(num3)
if temp > 0 and temp % 1 == 0:
    min6 = temp
else:
    min6 = float('inf')


print(min(min1,min2,min3,min4,min5,min6))

