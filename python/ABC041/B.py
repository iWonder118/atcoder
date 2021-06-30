mod = 10**9 + 7

a, b, c = map(int, input().split())
ans = a % mod
ans *= b
ans %= mod
ans *= c
ans %= mod
print(ans)
