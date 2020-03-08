import re

s = input()
if len(s) % 2 == 1:
  s += "a"
li = re.split('(..)',s)[1::2]
check = "hi"
ans = 0
for i in li:
  if check not in i:
    ans += 1
if ans == 0:
  print("Yes")
else:
  print("No")
