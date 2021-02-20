n, k = map(int, input().split())
for i in range(k):
    g1 = int("".join(sorted(list(str(n)), reverse=True)))
    g2 = int("".join(sorted(list(str(n)))))
    n = g1 - g2
print(n)
