n, a, b = map(int, input().split())
ans = 0
for i in range(1,n+1):
  total = 0
  for j in list(str(i)):
    total += int(j)
  if total >= a and total <= b: 
    ans += i
print(ans)