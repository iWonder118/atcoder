n, d = map(int, input().split())
x = [[0] * d] * n
x = [list(map(int, input().split())) for _ in range(n)]
for i in range(n-1):
  distance_total = 0
  for now_, next_ in zip(x[i], x[i + 1]):
    distance_total += (now_ - next_) ** 2