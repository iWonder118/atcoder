import itertools


n = int(input())
number = list(map(int, input().split()))

all = itertools.combinations(number, 2)
total = 0
for num in all:
    total += (num[0] - num[1]) ** 2
print(total)
