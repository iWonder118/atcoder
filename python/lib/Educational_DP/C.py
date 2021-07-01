n = int(input())
plans = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n + 1)]

for i in range(n):
    dp[i + 1][0] = max(dp[i][1] + plans[i][1], dp[i][2] + plans[i][2])
    dp[i + 1][1] = max(dp[i][0] + plans[i][0], dp[i][2] + plans[i][2])
    dp[i + 1][2] = max(dp[i][0] + plans[i][0], dp[i][1] + plans[i][1])
print(max(dp[n]))
