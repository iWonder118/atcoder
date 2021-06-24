def chmin(i, value):
    if dp[i] > value:
        dp[i] = value


n = int(input())
numbers = list(map(int, input().split()))
dp = [10 ** 5 + 1] * n
dp[0] = 0

for i in range(n):
    if i + 1 < n:
        chmin(i + 1, dp[i] + abs(numbers[i] - numbers[i + 1]))
    if i + 2 < n:
        chmin(i + 2, dp[i] + abs(numbers[i] - numbers[i + 2]))
print(dp[n - 1])
