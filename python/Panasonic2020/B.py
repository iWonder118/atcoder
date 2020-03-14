h, w = map(int, input().split())
boad = h * w
if w == 1 and h == 1:
  print(1)
else:
  print((boad + 1) // 2)
