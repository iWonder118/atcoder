import queue


def bfs(graph, s):
    n = len(graph)
    seen = [False] * n
    todo = queue.Queue()
    seen[s] = True
    todo.put(s)

    while not todo.empty():
        v = todo.get()
        
        for num in graph[v]:
            if seen[num]:
                continue
            seen[num] = True
            todo.put(num)


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(bfs(graph, 3))