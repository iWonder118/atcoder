from operator import add

n, m, x = map(int, input().split())
books = [list(map(int, input().split())) for _ in range(n)]
cost = []
for i in range(2 ** n):
  total = 0
  algo = [0] * m
  for j in range(n):
    if ((i >> j) & 1):
      algo = map(add, algo, books[j][1::])
      total += books[j][0]

  count = 0
  for k in algo:
    if k >= x:
      count += 1
  
  if count == m:
    cost.append(total)

if cost != []:
  print(min(cost))
else:
  print(-1)