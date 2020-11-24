sx, sy, gx, gy = map(int, input().split())
x_diff = abs(gx - sx)
y_diff = abs(sy) + abs(gy)
diff = x_diff / y_diff
if sx < gx:
    print(sx + diff * sy)
else:
    print(sx - diff * sy)
