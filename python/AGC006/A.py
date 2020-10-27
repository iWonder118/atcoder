n = int(input())
s = input()
t = input()
match_len = 0
if s == t:
    print(n)
else:
    for i, j in zip(range(n), range(n, 0, -1)):
        if s[i:] in t[:j]:
            match_len = len(s[i:])
    print(n * 2 - match_len)
