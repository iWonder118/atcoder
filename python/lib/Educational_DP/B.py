n, k = map(int, input().split())
numbers = list(map(int, input().split()))
dp = [10 ** 5 + 1] * n
dp[0] = 0

for i in range(1, n):
    if i == 1:
        dp[i] = abs(numbers[i] - numbers[i - 1])
    else:
        for j in range(1, k + 1):
            dp[i] = min(dp[i], dp[i - j] + abs(numbers[i - j] - numbers[i]))
print(dp[n - 1])
