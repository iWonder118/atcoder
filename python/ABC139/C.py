n = int(input())
h = list(map(int, input().split()))
count = 0
ans = []
for i in range(n - 1):
    if h[i] >= h[i + 1]:
        count += 1
    else:
        ans.append(count)
        count = 0
ans.append(count)
print(max(ans))
