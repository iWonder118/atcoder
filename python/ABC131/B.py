n, x = map(int, input().split())
l = list(map(int, input().split()))
total = 0
count = 0
for i in l:
  total += i
  if total <= x:
    count += 1
print(count + 1)