import math
from functools import reduce

def gcd(*numbers):
  return reduce(math.gcd, numbers)

k = int(input())
ans = 0
for i in range(1,k + 1):
  for j in range(1, k + 1):
    for k in range(1, k + 1):
      ans += gcd(i, j, k)
print(ans)
