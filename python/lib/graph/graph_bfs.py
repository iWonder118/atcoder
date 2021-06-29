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

    # 無向グラフの場合以下を追加
    # graph[b].append()
print(bfs(graph, 3))
# input
# 8 12
# 4 1
# 4 2
# 4 6
# 1 3
# 1 6
# 2 5
# 2 7
# 6 7
# 3 0
# 3 7
# 7 0
# 0 5
