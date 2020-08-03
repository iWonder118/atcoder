k = int(input())
number = 0

for i in range(1, k + 1):
    number = k * i
    count_7 = str(number).count("7")
    if count_7 == len(str(number)):
        print(count_7)
        exit()
print(-1)
