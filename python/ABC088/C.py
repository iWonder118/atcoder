field = [list(map(int, input().split())) for _ in range(3)]
for i in range(3):
    if i == 0:
        imin = 1
        imax = 2
    elif i == 1:
        imin = 0
        imax = 2
    elif i == 2:
        imin = 0
        imax = 1
    for j in range(3):
        if j == 0:
            jmin = 1
            jmax = 2
        elif j == 1:
            jmin = 0
            jmax = 2
        elif j == 2:
            jmin = 0
            jmax = 1

        a = field[imin][jmin]
        b = field[imin][jmax]
        c = field[imax][jmin]
        d = field[imax][jmax]
        if a + d != b + c:
            print("No")
            exit()
print("Yes")
