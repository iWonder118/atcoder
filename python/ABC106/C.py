s = list(input())
k = int(input())
for i in range(min(len(s), k)):
    if s[i] != "1":
        print(s[i])
        exit()
print(1)