n, m = map(int, input().split())
k = []
tube = []
for _ in range(m):
    k.append(int(input()))
    tube.append(list(map(int, input().split())))

for i in range(n)