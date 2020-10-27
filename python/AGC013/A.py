n = int(input())
array = list(map(int, input().split()))
upper_flg = 0
lower_flg = 0
ans = 0
for i in range(n - 1):
    diff = array[i + 1] - array[i]
    if diff > 0:
        if upper_flg > 0:
            upper_flg = 0
            ans += 1
        elif lower_flg >= 0:
            lower_flg += 1

    elif diff < 0:
        if lower_flg > 0:
            lower_flg = 0
            ans += 1
        elif upper_flg >= 0:
            upper_flg += 1
print(ans + 1)
