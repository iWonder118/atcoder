n = int(input())
bars = list(map(int, input().split()))
bars.sort(reverse=True)
count = 0
ans = 1
multi_count = 2
for i in range(0, len(bars) - 1):
    if bars[i] == bars[i + 1]:
        count += 1
    else:
        count = 0
    if count == 3:
        print(bars[i] ** 2)
        exit()
    elif count == 1:
        ans *= bars[i]
        multi_count -= 1
        if multi_count == 0:
            print(ans)
            exit()
print(0)