n = int(input())
names = [input().split() for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            if names[i][0] == names[j][0] and names[i][1] == names[j][1]:
                print("Yes")
                exit()
print("No")
