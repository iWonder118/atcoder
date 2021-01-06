n = int(input())
flowers = list(map(int, input().split()))
ans = 0
while flowers.count(0) != n:
    count = False
    for i in range(n):
        if flowers[i] > 0:
            flowers[i] -= 1
            count = True
        elif flowers[i] == 0 and count:
            ans += 1
            count = False
    if count:
        ans += 1

print(ans)
