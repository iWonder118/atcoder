x, k, d = map(int, input().split())

for i in range(k):
    if x < 0:
        if i % 2 == 1:
            print(abs(x + d))
            exit()
        else:
            print(abs(x))
            exit()
    x -= d
print(abs(x))
