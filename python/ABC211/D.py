n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    adj[a].append((b, 1))
    adj[b].append((a, 1))
