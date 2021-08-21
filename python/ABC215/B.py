import math


n = int(input())
for i in range(int(math.sqrt(n)) + 1):
    if 2 ** i <= n:
        ans = i
    else:
        break
print(ans)
