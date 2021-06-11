import itertools

N, M = map(int, input().split())
conditions = [tuple(map(int, input().split())) for i in range(M)]

K = int(input())
choices = [tuple(map(int, input().split())) for i in range(K)]
rs = 0

for balls in itertools.product(*choices):
    uniqueBalls = set(balls)

    count = 0
    for c1, c2 in conditions:
        if c1 in uniqueBalls and c2 in uniqueBalls:
            count += 1
    
    rs = max(rs, count)

print(rs)
