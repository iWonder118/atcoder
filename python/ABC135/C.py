n = int(input())
monsters = list(map(int, input().split()))
braves = list(map(int, input().split()))
destroys = 0

for i in range(n):
    double_m = monsters[i] + monsters[i + 1]
    if double_m <= braves[i]:
        destroys += braves