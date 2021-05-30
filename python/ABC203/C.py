n, k = map(int, input().split())
friends = [list(map(int, input().split())) for _ in range(n)]
friends = sorted(friends, key=lambda x: x[0])
diff = 0
before = 0
for i in range(n):
    diff = friends[i][0] - before
    if k - diff < 0:
        print(before + k)
        exit()
    k += friends[i][1] - diff
    before = friends[i][0]
print(k + before)
