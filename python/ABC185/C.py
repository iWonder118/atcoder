import math


L = int(input())
tmp = 1
for i in range(1, 12):
    tmp *= L - i
print(tmp // math.factorial(11))
