h, w = map(int, input().split())
fields = [list(input()) for _ in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        if fields[i][j] == ".":
            T = fields[i - 1][j] if 0 <= i - 1 else 0
            B = fields[i + 1][j] if i + 1 < h else 0
            L = fields[i][j - 1] if 0 <= j - 1 else 0
            R = fields[i][j + 1] if j + 1 < w else 0
            if T == ".":
                ans += 1
            if B == ".":
                ans += 1
            if L == ".":
                ans += 1
            if R == ".":
                ans += 1
print(ans // 2)
