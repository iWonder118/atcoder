n = int(input())
for i in range(1, 101):
    for j in range(1, 101):
        ans = (3 ** i) + (5 ** j)
        if ans == n:
            print("{} {}".format(i, j))
            exit()
print(-1)
