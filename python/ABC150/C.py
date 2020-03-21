import itertools

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

list_range = list(range(1,n+1))
pattern_list = list(itertools.permutations(list_range, n))
pattern_list.sort()
ans = [0] * 2
for i in range(len(pattern_list)):
  if p == q:
    break
  elif p == list(pattern_list[i]):
    ans[0] = i + 1
  elif q == list(pattern_list[i]):
    ans[1] = i + 1
print(abs(ans[0] - ans[1]))