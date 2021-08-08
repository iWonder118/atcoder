n = int(input())
numbers = list(map(int, input().split()))
sorted_numbers = sorted(numbers, reverse=True)
print(numbers.index(sorted_numbers[1]) + 1)
