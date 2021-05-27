from collections import Counter

N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)

ans = 0

for x in range(-200, 200 + 1):
    for y in range(x + 1, 200 + 1):
        xcnt = cnt[x]
        ycnt = cnt[y]
        total = xcnt * ycnt * (x - y) ** 2
        ans += total

print(ans)
