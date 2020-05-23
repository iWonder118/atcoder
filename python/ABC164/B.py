a, b, c, d = map(int, input().split())
while True:
  c -= b
  a -= d
  if c < 1:
    print("Yes")
    break
  elif a < 1:
    print("No")
    break