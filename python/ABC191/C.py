h, w = map(int, input().split())
graph = [list(input()) for _ in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        if graph[i][j] is "#":
            around = []
            count = 0
            for xi in range(-1, 2):
                for yj in range(-1, 2):
                    around.append([max(0, min(i + xi, w)), max(0, min(j + yj, h))])
            for point in around:
                if graph[point[0]][point[1]] is "#":
                    count += 1
            if count == 4:
                ans += 1
print(ans)