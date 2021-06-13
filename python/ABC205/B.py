n = int(input())
numbers = list(map(int, input().split()))
count = [0] * (n + 1)
count[0] = 1
for num in numbers:
    count[num] += 1
if 0 in count:
    print("No")
else:
    print("Yes")
