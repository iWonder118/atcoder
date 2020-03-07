n, a, b = map(int, input().split())
q = n // (a + b)
mod = n % (a + b)
if mod <= a:
  print(a * q + mod)
else:
  print(a * q)