n, k, m = map(int, input().split())
result = list(map(int, input().split()))
total = 0
for data in result:
  total += data
for i in range((k + 1)):
  averae = (total + i) / n
  if averae >= m:
    print(i)
    exit()
print(-1)