s, l, r = map(int, input().split())
if s >= l and s <= r:
  print(s)
elif s > r:
  print(r)
elif s < l:
  print(l)