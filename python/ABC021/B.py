N = int(input())
a, b = map(int, input().split())
K = int(input())
P = list(map(int, input().split()))
v = set([a, b])

for i in range(K):
    if P[i] in v:
        print("NO")
        exit()
    v.add(P[i])

print("YES")
