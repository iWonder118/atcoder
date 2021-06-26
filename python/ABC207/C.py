n = int(input())
path = [list(map(int, input().split())) for _ in range(n)]
count = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        souce_start = path[i][1]
        souce_end = path[i][2]
        dest_start = path[j][1]
        dest_end = path[j][2]
        if path[i][0] >= 3:
            souce_start += 0.9
        if path[i][0] % 2 == 0:
            souce_end -= 0.1
        if path[j][0] >= 3:
            dest_start += 0.9
        if path[j][0] % 2 == 0:
            dest_end -= 0.1
        if souce_start <= dest_end and dest_start <= souce_end:
            count += 1
print(count)
