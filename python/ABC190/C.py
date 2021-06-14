n, m = map(int, input().split())
conditions = []
for i in range(m):
    a, b = map(int, input().split())
    conditions.append([a - 1, b - 1])
k = int(input())
people = []
res = 0
for i in range(k):
    a, b = map(int, input().split())
    people.append([a - 1, b - 1])
for i in range(1 << k):
    dish = [0] * n
    for j in range(k):
        if (i >> j & 1):
            dish[people[j][0]] += 1
        else:
            dish[people[j][1]] += 1
    res_tmp = 0
    for j in range(m):
        if dish[conditions[j][0]] and dish[conditions[j][1]]:
            res_tmp += 1
    res = max(res, res_tmp)
print(res)
