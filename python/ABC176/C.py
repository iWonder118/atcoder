n = int(input())
a = list(map(int, input().split()))
total = 0
for i in range(n - 1):
    if a[i] > a[i + 1]:
        diff = abs(a[i] - a[i + 1])
        total += diff
        a[i + 1] += diff
        
print(total)
