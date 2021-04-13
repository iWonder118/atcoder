import math


r, x, y = map(int, input().split())
if math.sqrt(x ** 2 + y ** 2) == r:
    print(1)
elif r > x and r > y:
    print(2)
else:
    if math.sqrt(x ** 2 + y ** 2) % r == 0:
        print(int(math.sqrt(x ** 2 + y ** 2) // r))
    else:
        print(int(math.sqrt(x ** 2 + y ** 2) // r + 1))
