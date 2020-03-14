n = int(input())
s = [input() for i in range(n)]
ans = {}
word_list = list(set(s))

for i in word_list:
  ans[i] = s.count(i)

for k, v in sorted(ans.items()):
  if v == max(ans.values()):
    print(k)