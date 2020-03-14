n = int(input())
x = list(map(int, input().split()))
ans = []
for i in range(1,(max(x)+ 1)):
  total = 0
  for j in x:
    total += (j - i) ** 2
  ans.append(total)
print(min(ans))