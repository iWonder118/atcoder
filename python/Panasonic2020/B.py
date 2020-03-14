h, w = map(int, input().split())
boad = h * w
if boad < 4:
  print(1)
elif boad % 2 == 1 and boad > 3:
  print(boad // 2 + 1)
else:
  print(boad // 2)
