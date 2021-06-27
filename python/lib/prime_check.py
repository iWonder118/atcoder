import math


n = int(input())
is_prime = True
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        is_prime = False
print(is_prime)
