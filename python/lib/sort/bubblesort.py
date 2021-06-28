numbers = [8, 5, 3, 12, 14]
n = len(numbers)
for i in range(1, n):
    for j in range(n - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print(numbers)
