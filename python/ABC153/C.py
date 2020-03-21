n, k = map(int, input().split())
h = list(map(int, input().split()))
h.sort(reverse = True)
ans = 0
for enemy in h:
  if k > 0:
    k -= 1
  else:
    ans += enemy
print(ans)