
n = int(input())
line = list(map(int, input().split()))
count = 0
for i in range(n):
    result = []
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if line[i] != line[k] and line[i] != line[j] and line[j] != line[k]:
                _len = line[i] + line[k] + line[j]
                max_r = max(line[i], line[k], line[j])
                if max_r < _len - max_r:
                    count += 1
print(count)
