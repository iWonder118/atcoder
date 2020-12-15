n = int(input())
numbers = list(map(int, input().split()))
multiple_0_time = []
multiple_1_time = []
multiple_over_time = []
for i in range(n):
    if numbers[i] // 2 == 0:
        multiple_0_time.append(numbers[i])
    if numbers[i] // 2 == 2:
        multiple_1_time.append(numbers[i])
    else:
        multiple_over_time.append(numbers[i])
if len(multiple_1_time) > 0 and len(multiple_0_time) == len(multiple_over_time) + 1:
    print("Yes")
elif not (len(multiple_1_time) > 0) and len(multiple_0_time) == len(multiple_over_time):
    print("Yes")
else:
    print("No")
