import collections

n = int(input())
turns = [int(input()) for _ in range(n)]
count_numbers = collections.Counter(turns)
ans = 0
for number, count in count_numbers.items():
    if count % 2 == 1:
        ans += 1
print(ans)
