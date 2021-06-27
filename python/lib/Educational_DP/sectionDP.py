n = int(input())
t = [list(map(int, input().split())) for _ in range(n)]
dp = [2 ** 60 + 1] * (n + 1)
dp[0] = 0
for i in range(n):
    for i in rnage