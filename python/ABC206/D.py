n = int(input())
numbers = list(map(int, input().split()))
count = 0
if n % 2 == 1:
    before = numbers[:n // 2]
    after = numbers[(n // 2) + 1:]

else:
    before = numbers[:n // 2]
    after = numbers[n // 2:]

for b, a in zip(before, after[::-1]):
    if b != a:
        count += 1
print(max(count - 1, 0))