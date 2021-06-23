n = int(input())
numbers = list(map(int, input().split()))
dp = [10 ** 5 + 1] * n
dp[0] = 0

for i in range(1, n):
    if i == 1:
        dp[i] = abs(numbers[i] - numbers[i - 1])
    else:
        dp[i] = min(dp[i - 1] + abs(numbers[i] - numbers[i - 1]), dp[i - 2] + abs(numbers[i] - numbers[i - 2]))
print(dp[n - 1])
