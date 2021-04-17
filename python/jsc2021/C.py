import math


a, b = map(int, input().split())
ans = []
for i in range(a, b):
    for j in range(i + 1, b + 1):
        ans.append(math.gcd(i, j))
print(ans)
