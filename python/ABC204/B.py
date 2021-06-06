n = int(input())
trees = list(map(int, input().split()))
ans = 0
for i in range(n):
    nuts = trees[i] - 10
    if nuts > 0:
        ans += nuts
print(ans)
