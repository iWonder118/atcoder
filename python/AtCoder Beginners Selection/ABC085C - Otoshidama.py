n, yen = map(int,input().split())
yen1x104 = 10000
yen5x103 = 5000
yen1x103 = 1000
for i in range(n + 1):
  total = 0

  for j in range(n + 1 - i):
    k = (n - i- j)
    total = yen1x104 * i + yen5x103 * j + yen1x103 * k
    if yen - total == 0:
      print("{} {} {}".format(i, j, k))
      exit()
print("-1 -1 -1")