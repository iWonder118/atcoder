n, a, b = map(int, input().split())
ans = n // (a+b) * a
mod = n % (a+b)
print(ans + min(a, mod))