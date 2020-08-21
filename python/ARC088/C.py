x, y = map(int, input().split())

for i in range(1, 101):
    if x > y:
        ans = i - 1
        break
    x *= 2

print(ans)
