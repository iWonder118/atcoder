n = int(input())
s = list(input())
x = 0
ans = 0
for i in s:
  if i == "I":
    x += 1
  else:
    x -= 1
  ans = max(ans, x)

print(ans)