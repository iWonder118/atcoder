n, m = map(int, input().split())
edges = set()
for _ in range(m):
    a, b = map(int, input().split())
    edges.add((a, b))

ans = 'IMPOSSIBLE'
for i in range(2, n):
    if (1, i) in edges and (i, n) in edges:
        ans = 'POSSIBLE'
        break
print(ans)
