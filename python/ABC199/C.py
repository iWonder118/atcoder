n = int(input())
s = list(input())
q = int(input())
numbers = [list(map(int, input().split())) for _ in range(q)]

for i in range(q):
    if numbers[i][0] == 1:
        temp = s[numbers[i][1]]
        s[numbers[i][1]] = s[numbers[i][2]]
        s[numbers[i][2]] = temp
    else:
        str_s = "".join(s)
        print(str_s)
        s = list(str_s[n:] + str_s[:n + 1])

print("".join(s))