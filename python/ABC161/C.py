n, k = map(int,input().split())
nk_abs = abs(n - k)
if n < nk_abs and n < k:
  print(n)
  exit()
if k == 1:
  print(0)
else:
  print(n % nk_abs)