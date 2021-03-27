h, w, y, x = map(int, input().split())
words = [list(input()) for _ in range(h)]
ans = 0
x_count = 0
y_count = 0
flg = True
for i in range(h):
    if y - 1 < i and words[i][x - 1] == "#":
        ans += y_count
        flg = False
        break
    if words[i][x - 1] == ".":
        y_count += 1
    else:
        y_count = 0
if (flg):
    ans += y_count
flg = True
for i in range(w):
    if x - 1 < i and words[y - 1][i] == "#":
        ans += x_count
        flg = False
        break
    if words[y - 1][i] == ".":
        x_count += 1
    else:
        x_count = 0
if (flg):
    ans += x_count
print(ans - 1)
