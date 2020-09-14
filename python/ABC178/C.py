import itertools

count = 0
nums = list(range(10))
for v in itertools.permutations(nums):
    if 0 in v and 9 in v:
        count += 1

n = int(input())
n ** (10 ** 6)