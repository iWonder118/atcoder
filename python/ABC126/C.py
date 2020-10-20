n, k = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    continuous = i
    count = 0
    while k > continuous:
        continuous *= 2
        count += 1
    ans += (1 / n) * (0.5 ** count)
print("{:.12f}".format(ans))
# 0.999973749998
# 0.999973749998