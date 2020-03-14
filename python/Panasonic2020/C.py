import math

a, b, c = map(int,input().split())
d = math.sqrt(a) + math.sqrt(b)
if d < math.sqrt(c):
  print("Yes")
else:
  print("No")