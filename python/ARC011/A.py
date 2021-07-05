m, n, N = map(int, input().split())
ans = N
s = N
while s >= m:
    q, r = divmod(s, m)
    ans += n * q
    s = r
    s += n * q
print(ans)
