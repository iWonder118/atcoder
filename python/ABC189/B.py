n, x = map(int, input().split())
drinks = [list(map(int, input().split())) for _ in range(n)]
total = 0
for i in range(n):
    total += ((drinks[i][0] * drinks[i][1]) / 100) * (10 ** 6)
    if total > x * (10 ** 6):
        print(i + 1)
        exit()
print(-1)
