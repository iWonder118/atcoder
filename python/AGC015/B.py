buttons = list(input())
n = len(buttons)
ans = n - 1
for i in range(1, n):
    if buttons[i] == "U":
        ans += i * 2 + n - (i + 1)
    else:
        ans += i + (n - (i + 1)) * 2
print(ans) 