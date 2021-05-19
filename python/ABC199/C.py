n = int(input())
s = list(input())
q = int(input())
numbers = [list(map(int, input().split())) for _ in range(q)]
isReverse = True
for i in range(q):
    if numbers[i][0] == 1:
        temp = s[numbers[i][1] - 1]
        s[numbers[i][1] - 1] = s[numbers[i][2] - 1]
        s[numbers[i][2] - 1] = temp
    else:
        if isReverse:
            isReverse = False
        else:
            isReverse = True
ans = "".join(s)
if isReverse:
    print(ans[n:] + ans[:n])
else:
    print(ans)