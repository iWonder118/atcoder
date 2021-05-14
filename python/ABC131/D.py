n = int(input())
numbers = [list(map(int, input().split())) for _ in range(n)]
sorted_numbers = sorted(numbers, key=lambda x: x[1])
done = 0
for i in range(n):
    done += sorted_numbers[i][0]
    if not done <= sorted_numbers[i][1]:
        print("No")
        exit()
print("Yes")
