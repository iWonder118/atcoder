def chmax(i, j, value):
    if dp[i][j] < value:
        dp[i][j] = value


n, w = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (w + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(w + 1):
        if j - items[i][0] >= 0:
            chmax(i + 1, j, dp[i][j - items[i][0]] + items[i][1])
        chmax(i + 1, j, dp[i][j])
print(dp[n][w])
