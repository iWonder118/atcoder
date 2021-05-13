n = int(input())
numbers = list(map(int, input().split()))
sorted_number = sorted(numbers)

for i in range(n):
    if numbers[i] <= sorted_number[n // 2 - 1]:
        print(sorted_number[n // 2])
    else:
        print(sorted_number[n // 2 - 1])