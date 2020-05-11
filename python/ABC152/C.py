n = int(input())
p = list(map(int, input().split()))
ans=1
m=p[0]
for i in range(1,len(p)):
  if p[i]==1:
    ans=ans+1
    break
  elif p[i]>m:
    continue
  else:
    ans=ans+1
    m=p[i]
print(ans)