x, n = map(int, input().split())
if n != 0:
  n = list(map(int, input().split()))
  ans = []
  for i in range(101):
    if n.count(x + i) == 0:
      ans.append(x + i)

    if n.count(x - i) == 0:
      ans.append(x - i)
    
    if ans != []:
      break

  print(min(ans))
else:
  print(x)