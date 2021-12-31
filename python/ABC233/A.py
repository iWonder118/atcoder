x, y = list(map(int, input().split()))
diff = y - x
if diff < 0:
    diff = 0
if diff % 10 == 0:
    print(diff // 10)
else:
    print(diff // 10 + 1)
