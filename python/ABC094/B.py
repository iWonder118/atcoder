n, m, x = map(int, input().split())
A = list(map(int, input().split()))
cost = 0
goal = min(x, (n - x))
for i in range(m):
  if A[i] >= x and x < goal:
    cost += 1
  elif A[i] <= x and x > goal:
    cost += 1
print(cost)