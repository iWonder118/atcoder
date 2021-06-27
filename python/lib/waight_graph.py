n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b, w = map(int, input().split())
    graph[a].append({b: w})

    # 無向グラフの場合以下を追加
    # graph[b].append()
print(graph)
# input
# 8 12
# 4 1 1
# 4 2 2
# 4 6 3
# 1 3 4
# 1 6 5
# 2 5 6
# 2 7 7
# 6 7 8
# 3 0 9
# 3 7 10
# 7 0 11
# 0 5 12
