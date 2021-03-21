n = int(input())
count = 0
for i in range(1, 10 ** 6 + 1):
    if int(str(i) * 2) <= n:
        count += 1
print(count)
