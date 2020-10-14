n, t = map(int, input().split())
timing = list(map(int, input().split()))
total = 0
for i in range(n - 1):
    diff = timing[i + 1] - timing[i]
    total += min(t, diff)
print(total + t)
