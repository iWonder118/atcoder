import itertools


n, k = map(int, input().split())
times = [list(map(int, input().split())) for _ in range(n)]
nums = list(range(1, n))
ans = 0
for pattern in itertools.permutations(nums):
    total = 0
    before = 0
    for i in pattern:
        total += times[before][i]
        before = i
    total += times[before][0]
    if total == k:
        ans += 1
print(ans)
