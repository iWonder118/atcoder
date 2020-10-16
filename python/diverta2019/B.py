r, g, b, n = map(int, input().split())
ans = 0
for i in range(3001):
    for j in range(3001):
        rg_total = r * i + g * j
        if n >= rg_total and (n - rg_total) % b == 0:
            ans += 1
print(ans)
