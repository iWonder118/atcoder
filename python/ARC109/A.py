# def make_divisors(n):
#     lower_divisors, upper_divisors = [], []
#     i = 1
#     while i * i <= n:
#         if n % i == 0:
#             lower_divisors.append(i)
#             if i != n // i:
#                 upper_divisors.append(n // i)
#         i += 1
#     return lower_divisors + upper_divisors[::-1]
# max_num_divisor = make_divisors(max(s, p))
# for divisor in max_num_divisor:
#     plus = min(s, p) + divisor
#     multi = max(s, p) * divisor
#     if plus == multi:
#         print("Yes")
#         exit()
import math


s, p = map(int, input().split())
max_range = math.sqrt(10 ** 13)
for i in range(int(max_range)):
    if i * (s - i) == p:
        print("Yes")
        exit()
print("No")
