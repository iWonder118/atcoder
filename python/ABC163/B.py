n, m = map(int, input().split())
a = list(map(int, input().split()))
for i in range(m):
  n -= a[i]
if n >= 0:
  print(n)
else:
  print(-1)
