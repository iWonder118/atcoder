x = int(input())
temp = 0
for i in range(1,x + 1):
    temp += i
    if temp >= x:
        print(i)
        exit()