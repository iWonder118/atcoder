from functools import reduce


n = int(input())
numbers = list(map(int, input().split()))
ans = set()
ans.add(1)
for number in numbers:
    for i in range(2, 50):
        if number % i == 0:
            ans.add(i)
            break
print(reduce(lambda x, y: x * y, ans))