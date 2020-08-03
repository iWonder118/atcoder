import math

n, d = map(int, input().split())
fealds = [list(map(int, input().split())) for _ in range(n)]
count = 0
for i in range(n):
    distance = math.sqrt(fealds[i][0] ** 2 + fealds[i][1] ** 2)
    if distance <= d:
        count += 1
print(count)
