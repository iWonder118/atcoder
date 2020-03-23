s = input()
s_len = len(s)
s_reversed = s[::-1]
s_before = s[0:(s_len - 1) // 2:]
s_before_reversed = s_before[::-1]
s_after = s[((s_len + 3) // 2 - 1) : s_len:]
s_after_reversed = s_after[::-1]
if s == s_reversed and s_before == s_before_reversed and s_after == s_after_reversed:
  print("Yes")
else:
  print("No")