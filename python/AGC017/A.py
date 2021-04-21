n, p = map(int, input().split())
bisckets = list(map(int, input().split()))
ans = 0
for i in range(2 ** n):
    eat = []
    total = 0
    for j in range(n):
        if ((i >> j) & 1):
            eat.append(bisckets[j])
            total += bisckets[j]
    if (total % 2 == p):
        ans += 1
print(ans)