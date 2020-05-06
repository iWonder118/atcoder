import itertools
n, m, q = map(int, input().split())
num_lists = [list(map(int, input().split())) for _ in range(q)]
A = list(range(1, m+1))
ans = 0
for a in itertools.product(A, repeat=n):
  point = 0
  for num_list in num_lists:
    if num_list[2] == a[num_list[1] - 1] - a[num_list[0] - 1]:
      point += num_list[3]
  ans = max(ans, point)
print(ans)