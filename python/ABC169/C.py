from decimal import *
import math 

a, b = input().split()

result = Decimal(a) * Decimal(b)
print(math.floor(result))