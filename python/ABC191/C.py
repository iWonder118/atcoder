h, w = map(int, input().split())
graph = [list(input()) for _ in range(h)]
ans = 0
for i in range(h - 1):
    for j in range(w - 1):
        around = []
        count = 0
        for xi in range(2):
            for yj in range(2):
                around.append([i + xi, j + yj])
        for point in around:
            if graph[point[0]][point[1]] is "#":
                count += 1
        if count == 1 or count == 3:
            ans += 1
print(ans)