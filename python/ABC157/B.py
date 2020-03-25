a = []
[a.append(list(map(int, input().split()))) for _ in range(3)]
n = int(input())
b = [int(input())for _ in range(n)]
for i in b:
  for j in range(3):
    for k in range(3):
      if a[j][k] == i:
        a[j][k] = 1
ans = 0
count =0
for j in range(3):
  if a[j].count(1) == 3:
    ans += 1
  elif (a[0][j] == a[1][j] == a[2][j]) == 1:
    ans += 1
  elif (a[0][0] == a[1][1] == a[2][2]) == 1:
    ans += 1
  elif (a[0][2] == a[1][1] == a[2][0]) == 1:
    ans += 1
if ans > 0:
  print("Yes")
else:
  print("No")