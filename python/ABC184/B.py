n, x = map(int, input().split())
s = list(input())
for i in range(n):
    if s[i] == "x" and x > 0:
        x -= 1
    elif s[i] == "x" and x <= 0:
        continue
    else:
        x += 1
print(x)
