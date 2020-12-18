import math


a, b, c, d = map(int, input().split())
c_number = b // c - (a - 1) // c
d_number = b // d - (a - 1) // d
lcm = c * d // math.gcd(c, d)
cdx = b // lcm - (a - 1) // lcm
print((b - a + 1) - c_number - d_number + cdx)
