n, m, t = map(int, input().split())
timing = [list(map(int, input().split())) for _ in range(m)]
batery = n
before = 0
for i in range(m):
    batery -= timing[i][0] - before
    if batery <= 0:
        print("No")
        exit()
    batery += timing[i][1] - timing[i][0]
    before = timing[i][1]
    batery = min(n, batery)
if before + batery - t < 1:
    print("No")
else:
    print("Yes")
