from math import factorial
n, m = map(int, input().split())
all_bolls = n + m
all_patterns = factorial(all_bolls) // factorial(2) // factorial(all_bolls - 2)
print(all_patterns - n * m)