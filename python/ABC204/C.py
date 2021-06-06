n, m = map(int, input().split())
routes = [list(map(int, input().split())) for _ in range(m)]
ans = n
dp = [0] * (n + 1)
for i in range(m):
    dp[routes[i][0]] += 1
    dp[routes[i][1]] += 1

if m != 0:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dp[i] != 0 and dp[j] != 0:
                if i != j and abs(dp[i] - dp[j]) <= 1:
                    ans += 1
print(ans)
