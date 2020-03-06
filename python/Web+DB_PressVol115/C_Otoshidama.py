import sys

n, y = map(int, input().split())
for i in range(n+1):
  for j in range(n-i+1):
    k = n - i - j
    money = 10000 * i + 5000 * j + 1000 * k
    if y == money:
      print("{} {} {}".format(i, j, k))
      sys.exit()
print(-1, -1, -1)