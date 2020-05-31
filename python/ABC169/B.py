n = int(input())
a = list(map(int, input().split()))
if a.count(0) > 0:
  ans = 0
else:
  ans = 1

for i in a:
  ans *= i
  if ans > (10 ** 18):
    break

if not ans > (10 ** 18):
  print(ans)
else:
  print(-1)