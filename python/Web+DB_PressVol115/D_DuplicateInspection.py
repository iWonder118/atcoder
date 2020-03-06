n = int(input())
a = [int(input()) for i in range(n)]
a.sort()
ans = [0, 0]
for i in range(1, n+1):
  if a.count(i) == 0:
    ans[0] = i
  elif a.count(i) == 2:
    ans[1] = i
if ans[0] == 0:
  print("Correct")
else:
  print("{1} {0}".format(ans[0], ans[1]))