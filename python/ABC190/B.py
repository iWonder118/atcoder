n, s, d = map(int, input().split())
magics = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    if s > magics[i][0] and magics[i][1] > d:
        print("Yes")
        exit()
print("No")
