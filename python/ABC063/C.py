n = int(input())
points = [int(input()) for _ in range(n)]
ten_multiple = []
other = []
total = 0
for point in points:
    total += point
    if point % 10 == 0:
        ten_multiple.append(point)
    else:
        other.append(point)
if len(ten_multiple) == n:
    print(0)
elif total % 10 == 0:
    print(total - min(other))
else:
    print(total)
