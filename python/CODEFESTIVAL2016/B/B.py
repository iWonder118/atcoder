n, a, b = map(int, input().split())
s = list(input())
for i in s:
  if i == "a" and (a + b) != 0:
    a -= 1
    print("Yes")
  elif i == "b" and (a + b) != 0 and b != 0:
    b -=1
    print("Yes")
  else:
    print("No")