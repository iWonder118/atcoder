n, a, b = map(int, input().split())
min_num = a * (n - 1) + b
max_num = b * (n - 1) + a
ans = max_num - min_num
if ans < 0:
    print(0)
else:
    print(ans + 1)
