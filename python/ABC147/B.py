s = list(input())
s_len = len(s)
ans = 0
if s_len % 2 == 0:
  for i, j in zip(s[0 : (s_len // 2 )], reversed(s[(s_len // 2) : s_len + 1])):
    if i != j:
      ans += 1
else:
  for i, j in zip(s[0 : (s_len // 2  )], reversed(s[(s_len // 2 + 1) : s_len])):
    if i != j:
      ans += 1
print(ans)