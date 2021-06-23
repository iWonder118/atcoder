def template(i, value):
    if dp[i] > value:
        dp[i] = value


n = int(input())
numbers = list(map(int, input().split()))
dp = [10 ** 5 + 1] * n
dp[0] = 0

for i in range(1, n):
    template(i, dp[i - 1] + abs(numbers[i] - numbers[i - 1]))
    if i > 1:
        template(i, dp[i - 2] + abs(numbers[i] - numbers[i - 2]))
print(dp[n - 1])
