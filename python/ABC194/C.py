n = int(input())
numbers = list(map(int, input().split()))

total = 0
sum_A = sum_A2 = 0
for i in range(n):
    total += i * numbers[i]**2 - 2 * numbers[i] * sum_A + sum_A2
    sum_A += numbers[i]
    sum_A2 += numbers[i] ** 2

print(total)