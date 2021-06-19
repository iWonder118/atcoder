n = int(input())
ans = 1
money = 0
for i in range(1, n + 1):
    money += i
    if money >= n:
        print(ans)
        exit()
    ans += 1
