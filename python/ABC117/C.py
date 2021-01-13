n, m = map(int, input().split())
positions = list(map(int, input().split()))
positions.sort()
diffs = []
if 1 < n:
    for i in range(m - 1):
        diffs.append(abs(positions[i + 1] - positions[i]))
    toral_diff = sum(diffs)
    diffs.sort()
    ans = toral_diff - sum(diffs[-(n - 1):])
else:
    ans = max(positions) - min(positions)
print(ans)
