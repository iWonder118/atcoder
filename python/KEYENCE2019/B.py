s = input()
key = "keyence"
ans = False
for i in range(8):
    if (key[:i] == s[:i] and key[i:] == s[i + (len(s) - 7):]):
        ans = True
if(ans):
    print("YES")
else:
    print("NO")
