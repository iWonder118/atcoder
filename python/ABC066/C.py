n = int(input())
numbers = list(map(int, input().split()))
odd = []
even = []
for i in range(n):
    if i % 2 == 0:
        odd.append(numbers[i])
    else:
        even.append(numbers[i])
if n % 2 == 0:
    even.reverse()
    even.extend(odd)
    print(" ".join(map(str, even)))
else:
    odd.reverse()
    odd.extend(even)
    print(" ".join(map(str, odd)))