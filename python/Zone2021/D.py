s = list(input())
t = []
for i in range(len(s)):
    if s[i] == "R":
        t.reverse()
    elif t != []:
        t_pop = t.pop()
        if t_pop != s[i]:
            t.append(t_pop)
            t.append(s[i])
print("".join(t))
