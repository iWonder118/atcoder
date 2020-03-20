n = int(input())
mochi = [int(input()) for _ in range(n)]
mochi.append(0)
mochi.sort(reverse = True)
ans = 0
for i in range(n):
  if mochi[i] > mochi[i+1]:
    ans += 1
print(ans)