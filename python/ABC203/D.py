n, k = map(int, input().split())
fields = [list(map(int, input().split())) for _ in range(n)]
ans = 801
for ni in range(n - k + 1):
    for nj in range(n - k + 1):
        pond = []
        for ki in range(k):
            for kj in range(k):
                pond.append(fields[ni + ki][nj + kj])
        if k % 2 == 0:
            ans = min(pond[k ** 2 // k], ans)
        else:
            ans = min(pond[k ** 2 // k + 1], ans)
print(ans)
