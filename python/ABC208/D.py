def warshall_floyd(graph):
    for k in range(n + 1):
        for i in range(n + 1):
            for j in range(n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph


n, m = map(int, input().split())
INF = 10 ** 9 + 1
graph = [[INF] * n for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = c
ans = 0
for i in range(n):
    graph[i][i] = 0
for k in range(n):
    _next = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            _next[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            if INF != graph[i][j]:
                ans += graph[i][j]
    graph = _next
print(ans)
