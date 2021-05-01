n, d, h = map(int, input().split())
ans = 0
buildings = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    tilt = (h - buildings[i][1]) / (d - buildings[i][0])
    ans = max(ans, h - tilt * d)
print(ans)