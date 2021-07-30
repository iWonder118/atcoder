from collections import Counter

s = list(input())
len_s = len(s)
mod = 10 ** 9 + 7
s_Count = dict(Counter(s))
ans = 1
chokudai_index = dict()
for c in list("chokudai"):
    chokudai_index[c] = s.index(c)
    s[c]
print(ans)
