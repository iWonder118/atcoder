s, t = input().split()
a, b = map(int, input().split())
u = input()
if u == s:
  print("{} {}".format(a-1, b))
else:
  print("{} {}".format(a, b-1))