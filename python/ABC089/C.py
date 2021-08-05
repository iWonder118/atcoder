import itertools
 
n = int(input())
cap = 'MARCH'
d = dict()
ans = 0

for _ in range(n):
    s = input()
    if s[0] in cap:
        if s[0] in d:
            d[s[0]] += 1
        else:
            d[s[0]] = 1
            
for c in itertools.combinations(d, 3):
    ans += d[c[0]] * d[c[1]] * d[c[2]]
print(ans)
