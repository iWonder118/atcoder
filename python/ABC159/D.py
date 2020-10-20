import collections

n = int(input())
balls = list(map(int, input().split()))
count_balls = collections.Counter(balls)
tot = 0
for key in count_balls:
    tot += count_balls[key] * (count_balls[key] - 1)
tot //= 2

for i in range(n):
    print(tot - count_balls[balls[i]] + 1)
