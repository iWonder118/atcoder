a, b, c, k = map(int, input().split())
is_odd = k % 2
if is_odd == 0:
    ans = a - b
else:
    ans = b - a
if ans > 10 ** 18:
    print("Unfair")
else:
    print(ans)
