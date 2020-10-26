n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(m)]
connect = [[0] * n] * m
