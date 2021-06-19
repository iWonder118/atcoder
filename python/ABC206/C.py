n = int(input())
numbers = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i, n):
        if numbers[i] != numbers[j]:
            ans += 1
print(ans)