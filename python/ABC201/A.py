numbers = list(map(int, input().split()))
numbers.sort()

if numbers[2] - numbers[1] == numbers[1] - numbers[0]:
    print("Yes")
else:
    print("No")