h, n = map(int, input().split())
Deathblow = list(map(int, input().split()))
for i in range(n):
  h -= Deathblow[i]
if h < 1:
  print("Yes")
else:
  print("No")