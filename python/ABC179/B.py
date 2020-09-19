n = int(input())
results = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    if ans >= 3:
        break
    if results[i][0] == results[i][1]:
        ans += 1
    else:
        ans = 0
if ans >= 3:
    print("Yes")
else:
    print("No")
