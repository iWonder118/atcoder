n = int(input())
ans = []
for i in range(2, 10 ** 5 + 1):
    for j in range(2, 35):
        if i ** j <= n:
            ans.append(i ** j)
print(n - len(set(ans)))
