h, w = map(int, input().split())
feald = [input().split() for _ in range(h)]
print(feald)
for i in feald:
  for j in list(i):
    if 