x = int(input())
m = int(input())
x_max = max(map(int, (list(str(x)))))
print(x_max)
count = 0
while True:
    x_max += 1
    if m < int(str(x), x_max):
        break
    count += 2
print(count)
