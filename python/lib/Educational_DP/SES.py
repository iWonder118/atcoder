s = list(input())
t = list(input())
len_s = len(s) + 1
len_t = len(t) + 1
dp = [[10 ** 5 + 1] * len_t for _ in range(len_s)]
dp[0][0] = 0
for i in range(len_s):
    for j in range(len_t):
        if i > 0 and j > 0:
            if s[i - 1] == t[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
            else:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)
        if i > 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
        if j > 0:
            dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
print(dp[len_s - 1][len_t - 1])
