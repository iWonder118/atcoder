numbers = list(map(int, input().split()))
ans = 0
for num in numbers:
    if num == 1:
        ans += 6
    elif num == 2:
        ans += 5
    elif num == 3:
        ans += 4
    elif num == 4:
        ans += 3
    elif num == 5:
        ans += 2
    else:
        ans += 1
print(ans)
