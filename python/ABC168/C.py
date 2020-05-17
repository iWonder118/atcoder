import math

a, b, h, m = map(int, input().split())
angule_h = 30 * h + 0.5 * m
angule_m = 6 * m
angule_diff = min(360 - abs(angule_h - angule_m),abs(angule_h - angule_m))
c_2 = (a ** 2 + b ** 2) - (2 * a * b * math.cos(math.radians(angule_diff)))
print(math.sqrt(c_2))