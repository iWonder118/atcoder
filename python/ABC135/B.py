n = int(input())
p = list(map(int, input().split()))
p_sort = sorted(p)
count = 0
for a, b in zip(p, p_sort):
  if a == b:
    count += 1
if len(p) - count <= 2:
  print("YES")
else:
  print("NO")