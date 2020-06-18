x, y = map(int, input().split())
for i in range(x+1):
  f = 2 * i + 4 * (x - i)
  if f == y:
    print("Yes")
    exit()

print("No")