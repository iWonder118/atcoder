import math
n = int(input())

for i in range(1, n + 1):

    ans = 0
    i /= 2
    ran = int(math.sqrt(i))
    if ran < 1:
        ran = 1
    for x in range(1, ran + 1):
        for y in range(1, ran + 1):
            for z in range(1, ran + 1):
                xyz = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
                if i == xyz:
                    ans += 1
    print(ans)
