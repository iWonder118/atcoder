n = int(input())
stores = [list(map(int, input().split())) for _ in range(n)]
ans = []
for i in range(n):
    if stores[i][0] < stores[i][2]:
        ans.append(stores[i][1])
if ans == []:
    print(-1)
else:
    print(min(ans))
