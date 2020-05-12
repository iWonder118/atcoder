n, m, c = map(int, input().split())
b = list(map(int, input().split()))
code_list = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for code in code_list:
  total = 0
  for i, j in zip(code, b):
    total += i * j 
  if (total + c) > 0:
    ans += 1
print(ans)