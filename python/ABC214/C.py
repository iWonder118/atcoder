n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
INF = 10 ** 9 + 1
dp = [INF] * (n + 1)
dp[0] = t[0]
for i in range(n - 1):
    dp[i + 1] = min(dp[i] + s[i], t[i + 1])

for i in range(n):
    print(dp[i])
