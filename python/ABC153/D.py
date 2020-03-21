H = int(input())
ans = 0
ms = [(H, 1)]
while ms:
  m, c = ms.pop()
  ans += c
  if m > 1:
    ms.append((m // 2, c * 2))
print(ans)