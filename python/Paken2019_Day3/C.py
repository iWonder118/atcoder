n, m = map(int, input().split())
group = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(m):
    for j in range(m):
        tmp = 0
        for k in range(n):
            if i != j:
                tmp += max(group[k][i], group[k][j])
        ans = max(ans, tmp)
print(ans)
