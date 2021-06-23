def rec(i):
    if dp[i] < 10 ** 5 + 1:
        return dp[i]
    template(i, rec(i - 1) + abs(numbers[i] - numbers[i - 1]))
    if i > 1:
        template(i, rec(i - 2) + abs(numbers[i] - numbers[i - 2]))
    return dp[i]


def template(i, value):
    if dp[i] > value:
        dp[i] = value


n = int(input())
numbers = list(map(int, input().split()))
dp = [10 ** 5 + 1] * n
dp[0] = 0
print(rec(n - 1))
