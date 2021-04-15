n = int(input())
numbers = list(map(int, input().split()))
odd = []
even = []
for i in range(n):
    if i % 2 == 0:
        odd.append(numbers[i])
    else:
        even.append(numbers[i])
ans = list(reversed(even)).extend(odd)
print(" ".join(map(str, ans)))
    