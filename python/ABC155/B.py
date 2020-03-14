n  = int(input())
A = list(map(int,input().split()))
ans = []
A_even = [i for i in A if i % 2 == 0]
for i in A_even:
  if i % 3 == 0 or i % 5 == 0:
    ans.append(i)
if len(ans) == len(A_even):
  print("APPROVED")
else:
  print("DENIED")