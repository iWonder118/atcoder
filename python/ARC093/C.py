n = int(input())
numbers = [0]
numbers.extend(list(map(int, input().split())))
numbers.append(0)
total = 0
for i in range(n + 1):
    total += abs(numbers[i] - numbers[i + 1])

for i in range(1, n + 1):
    ans = total
    ans -= abs(numbers[i - 1] - numbers[i])
    ans -= abs(numbers[i] - numbers[i + 1])
    ans += abs(numbers[i - 1] - numbers[i + 1])
    print(ans)