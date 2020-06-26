import collections
import string

s = input()
s_count = collections.Counter(s)
s_list = list(s_count.keys())
ans = []

for alphabet in list(string.ascii_lowercase):
  if not alphabet in s_list:
    ans.append(alphabet)
if ans != []:
  print(ans[0])
else:
  print("None")