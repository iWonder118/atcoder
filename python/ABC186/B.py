h, w = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(h)]
total = 0
min_num = 101
for i in range(h):
    min_num = min(min(field[i]), min_num)
    total += sum(field[i])
ans = total - h * w * min_num
print(ans)
