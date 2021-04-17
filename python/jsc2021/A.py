x, y, z = map(int, input().split())
if (y / x * z) % 1 == 0:
    print(int(y / x * z) - 1)
else:
    print(int(y / x * z))
