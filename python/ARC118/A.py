t, N = map(int, input().split())

handled = [False] * (100 + t)
for i in range(1, 100):
    handled[int(i * (100 + t) / 100)] = True

unhandled = []
for i in range(1, 100 + t):
    if not handled[i]:
        unhandled.append(i)

x, y = divmod(N - 1, len(unhandled))
print((100 + t) * x + unhandled[y])
