import collections

n = int(input())
p = list(map(int, input().split()))
ans = [0] * n
count_list = collections.Counter(p)
ans[0] = count_list[p[0]]

for key, value in count_list:
  p.index[key]