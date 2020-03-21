from collections import Counter

n = int(input())
a = list(map(int, input().split()))
ans = max(Counter(a).values())
if ans < 2:
  print("YES")
else:
  print("NO")
