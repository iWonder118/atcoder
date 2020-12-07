import math
from functools import reduce


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


n = int(input())
ans = 1
nums = list(range(2, n + 1))
ans += lcm_list(nums)
print(ans)
