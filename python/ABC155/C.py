from collections import Counter

n = int(input())
s = [input() for i in range(n)]
ans = []

charctor_count = Counter(s)
max_count = max(charctor_count.values())
for k, v in charctor_count.items():
  if v == max_count:
    ans.insert(0, k)
for out in ans:
  print(out)