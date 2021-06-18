import sys
sys.setrecursionlimit(10**6)


def dfs(v):
    seens[v] = True
    gpr[v] = ptr
    for nv in g[v]:
        if seens[nv]:
            continue
        dfs(nv)


n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

seens = [False] * n
gpr = [-1] * n
ptr = 0

for v in range(n):

    if seens[v]:
        continue
    else:
        ptr += 1
        dfs(v)
        
print(len(set(gpr)) - 1)
