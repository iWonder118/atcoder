n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
ans = []
for i in range(n):
    for j in range(i + 1, n):
        x_diff = points[i][0] - points[j][0]
        y_diff = points[i][1] - points[j][1]
        if i != j:
            if y_diff == 0:
                tmp = x_diff
            else:
                tmp = x_diff / y_diff
            if abs(tmp) >= 1:
                ans.append(tmp)
print(len(ans))
