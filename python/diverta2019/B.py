r, g, b, n = map(int,input().split())
ans = 0
for i in range(3001):
    for j in range(3001):
        if (n-r*i-g*j) < 0:
            continue
        if (n - r * i - g * j) % b == 0:
            ans += 1
print(ans)