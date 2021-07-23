import collections
 
n = int(input())
li = list(map(int,input().split()))
cnt = 0
for i in range(n-1):
    if li[i] == i+1: 
        li[i],li[i+1] = li[i+1],li[i]
        cnt += 1
if li[n-1] == n:
    cnt += 1
print(cnt)