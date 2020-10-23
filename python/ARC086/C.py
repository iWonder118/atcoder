import collections

n, k = map(int, input().split())
balls = list(map(int, input().split()))
count_balls = collections.Counter(balls)
count_kind = len(count_balls.values())
diff = count_kind - k
if diff >= 0:
    print(sum(sorted(count_balls.values(), reverse=True)[k:]))
else:
    print(0)
