import collections

n = int(input())
a = list(map(int, input().split()))
q = int(input())
bc = [list(map(int, input().split())) for _ in range(q)]
ans_count = []
total = 0
for i in range(n):
  total += a[i]

count = collections.Counter(a)
for i in range(q):
  num = count[bc[i][0]]
  count[bc[i][0]] = 0
  count[bc[i][1]] += num
  total += (bc[i][1] - bc[i][0]) * num
  print(total)