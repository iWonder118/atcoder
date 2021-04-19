n, m = map(int, input().split())
ans = 0
if n < m:
    m -= n * 2
    ans += n + m // 4
else:
    ans = m // 2
print(ans)