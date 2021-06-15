import itertools


numbers = list(map(int, input().split()))
x = []
for i in itertools.permutations(numbers, 3):
    x.append(sum(i))
print(sorted(set(x), reverse=True)[2])
