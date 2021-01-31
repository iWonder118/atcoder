n, m = map(int, input().split())
conditions = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
man = [list(map(int, input().split())) for _ in range(k)]
dishs = [0] * 17
tmp = []
for i in range(k):
    dishs[man[i][0]] += 1
    dishs[man[i][1]] += 1

ans = 0
for condition in conditions:
    if 0 < dishs[condition[0]] and 0 < dishs[condition[1]]:
        ans += 1
print(ans)
