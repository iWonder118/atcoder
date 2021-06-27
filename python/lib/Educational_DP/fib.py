def fib(n):
    if memo[n] != 0:
        return memo[n]
    if n <= 1:
        return 1
    memo[n] = fib(n - 2) + fib(n - 1)
    return memo[n]


n = int(input())
memo = [0] * (n + 1)
print(fib(n))
