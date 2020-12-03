a, b, x, y = map(int, input().split())
print(int(abs(2 * b + 1 - 2 * a) / 2) * min(2 * x, y) + x)
