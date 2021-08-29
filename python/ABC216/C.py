n = int(input())
count = 1
ans = []
while count <= 120:
    isEven = n % 2 == 0
    if n / 2 <= n - 1 and isEven:
        n = n // 2
        ans.append("B")
    else:
        n -= 1
        ans.append("A")
    if n == 0:
        break
    count += 1

print("".join(reversed(ans)))
