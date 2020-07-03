n = int(input())
lucas_number = [0] * (n + 1)
lucas_number[0] = 2
lucas_number[1] = 1
for i in range(2, n + 1):
    lucas_number[i] = lucas_number[i - 1] + lucas_number[i - 2]
print(lucas_number[n])
