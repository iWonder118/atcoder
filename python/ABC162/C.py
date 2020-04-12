import math
from functools import reduce
import itertools

def gcd(*numbers):
  return reduce(math.gcd, numbers)

n = int(input())
ans = 0
A = list(range(1,n + 1))
for numbers in itertools.product(A, repeat=3):
  ans += gcd(numbers[0], numbers[1], numbers[2])

print(ans)
