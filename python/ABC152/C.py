n = int(input())
p = list(map(int, input().split()))
p.insert(0,0)
count = 0
for i in range(1, n+1):
  for j in range(1, i+1):
    if p[i] < p[j]:
      count += 1
      break
print(count)