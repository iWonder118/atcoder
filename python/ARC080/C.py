n = int(input())
numbers = list(map(int, input().split()))
multiple_4 = []
multiple_2 = []
other = []
for i in range(n):
    if numbers[i] % 4 == 0:
        multiple_4.append(numbers[i])
    elif numbers[i] % 2 == 0:
        multiple_2.append(numbers[i])
    else:
        other.append(numbers[i])
if len(multiple_2) == 0 and len(other) <= len(multiple_4) + 1:
    print("Yes")
elif len(multiple_2) != 0 and len(other) <= len(multiple_4):
    print("Yes")
else:
    print("No")
