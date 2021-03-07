import math


K = int(input())
sqrt_k = int(math.sqrt(K))
ans = 0
for i in range(1, K + 1):
    for j in range(1,sqrt_k + 1):
        for k in range(1, sqrt_k + 1):
            if i * j * k <= K:
                if i == j and j == k:
                    ans += 1
                elif i == j or j == k:
                    ans += 2
                else:
                    ans += 3
print(ans)