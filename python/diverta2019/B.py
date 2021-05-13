import math


r, g, b, n = map(int, input().split())
ans = 0
for i in range(math.floor(n // r) + 1):
    red = r * i
    for j in range(math.floor((n - red) // g) + 1):
        green = g * j
        if (n - red - green) % b == 0:
            ans += 1
print(ans)