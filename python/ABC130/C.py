w, h, x, y = map(int, input().split())
if w / 2 == x and h / 2 == y:
    print("{:.6f} 1".format(w * h / 2))
else:
    print("{:.6f} 0".format(w * h / 2))