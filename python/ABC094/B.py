n, m, x = map(int, input().split())
A = list(map(int, input().split()))
cost = 0
for i in range(x, n+1):
  if A.count(i) > 0:
    cost += 1
cost_nomal = cost
cost = 0 
for i in range(1, x+1):
  if A.count(i) > 0:
    cost += 1
cost_reverse = cost

print(min(cost_nomal,cost_reverse))