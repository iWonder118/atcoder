l, r, d = map(int, input().split())
numbers = list(range(l, r + 1))
ans = []
for i in numbers:
    if i % d == 0:
        ans.append(i)
print(len(ans))
