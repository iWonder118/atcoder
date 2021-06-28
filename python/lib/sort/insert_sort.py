# n = int(input())
# numbers = list(map(int, input().split()))
numbers = [8, 5, 3, 12, 14]
n = len(numbers)

for i in range(1, n):
    target = numbers[i]
    j = i - 1
    while j >= 0 and numbers[j] > target:
        numbers[j + 1] = numbers[j]
        j -= 1
    numbers[j + 1] = target

print(numbers)
