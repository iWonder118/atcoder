n, m = map(int, input().split())
numbers = [list(map(int, input().split())) for _ in range(m)]
if n == 1:
    start = 0
else:
    start = 10 ** (n - 1)

for i in range(start, 10 ** n):
    number = str(i)
    count = 0
    for j in range(m):
        if number[numbers[j][0] - 1] == str(numbers[j][1]):
            count += 1
    if count == m:
        print(number)
        exit()
print(-1)
