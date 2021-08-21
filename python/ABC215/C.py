import itertools


s, k = input().split()
s = list(s)
k = int(k)
s_patterns = sorted(set([''.join(v) for v in itertools.permutations(s)]))
print(s_patterns[k - 1])
