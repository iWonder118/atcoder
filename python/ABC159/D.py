import collections
from math import factorial

n = int(input())
a = list(map(int, input().split()))
k_pop_len = len(a) - 1
for k in range(len(a)):
  none_k = a.pop(k)
  collections.Counter(none_k)
  all_patterns = factorial(k_pop_len) // factorial(2) // factorial(k_pop_len - 2)
  print(all_patterns - )