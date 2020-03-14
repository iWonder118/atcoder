from collections import Counter
n=int(input())
s=[]
for _ in range(n):
    s.append(input())
c = Counter(s)
ans=[]
max_vote = max(c.values())
for i,j in c.items():
    if j == max_vote:
        ans.append(i)
print("\n".join(sorted(ans)))