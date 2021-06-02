S = input()

target = "AKIHABARA"

if len(S) > len(target):
    print("NO")
    exit()

for i, c in enumerate(target):
    if i >= len(S):
        sc = ""
    else:
        sc = S[i]
    if sc != c:
        S = S[0:i] + "A" + S[i:]

if S == target:
    print("YES")
else:
    print("NO")
