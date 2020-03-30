n = int(input())
s = list(input())
for i in range(len(s)):
  rot_n = ord(s[i]) + n
  if rot_n > 90:
    rot_n -= 26
  s[i] = chr(rot_n)
print("".join(s))