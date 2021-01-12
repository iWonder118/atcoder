k, a, b = map(int, input().split())
if a + 1 >= b or a - 1 >= k:
    print(k + 1)
else:
    diff = b - a
    time = (k - a + 1) // 2
    mod = (k - a + 1) % 2
    print(a + diff * time + mod)
