a, b, c, d = map(int, input().split())
blue = a
red = 0
count = 0
for i in range(1, 10 ** 5 + 1):
    blue += b
    red += c
    count = i
    if blue / red <= d:
        print(i)
        exit()
print(-1)
